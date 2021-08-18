with open("WordDictionary.txt", "rb") as WD_file:
    with open("BadWords.txt", "rb") as BW_file:
        with open("BadWordsGoogle.txt", "rb") as BWG_file:
            with open("BadWordsFB.txt", "rb") as BWFB_file:
                with open("BadWordsYT.txt", "rb") as BWYT_file:
                    WD_set = set(WD_file.read().splitlines())
                    BWOG_set = set(BW_file.read().splitlines())
                    BWG_set = set(BWG_file.read().splitlines())
                    BWFB_set = set(BWFB_file.read().split(b", "))
                    BWYT_set = set(BWYT_file.read().split(b", "))
                    BW_set = BWG_set | BWFB_set | BWYT_set
                    omitted_words = [word.decode() for word in BW_set if word in WD_set and word not in BWOG_set]
                    print(*omitted_words, sep="\n")
                    print(f"Count: {len(omitted_words)}")
