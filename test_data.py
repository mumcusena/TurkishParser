correct_tests_sentences = ["sen yavaşça mama ye di n",
                    "yüksek ses le müzik dinle me",
                    "kitap ı nı getir me sin",
                    "kitap ı al dı -",
                    "ben kedi m le okul a git ti m",
                    "siyah kedi yarın gel ecek mi",
                    "bu ağaç ın altında her gece mehtap ı izle r di k",
                    "destan lar milli kültür ümüz ü ve tarih imiz i anlat ır",
                    "dün arkadaş ım a bir hediye al dı m",
                    "tarihi roman lar ı keyif le oku yor um.",
                    "ben dün akşam yemek i için anne m e yardımet ti m",
                    "yaz meyve ler i den karpuz bence en güzel meyve dir",
                    "buakşam ki toplantı a katıl acak mı sınız",
                    "siz bura a enson nezaman gel di niz",
                    "okul biz im köy e epeyce uzak ta dı",
                    "yüksek ses le müzik dinle me"
                   ]

false_tests_sentences = ["sen yavaşça mama ye di m",
                        # "anne m bugün okul a git ti n" 
                        "ben arkadaş ım a hediye al dı n",
                        "tarihi bir roman lar oku du m",
                        "dün baba m a yardımet ecek im",
                        "ben okul git ti m",
                        "ben kitap oku n du",
                        "ben okul da git ti m"
                   ]

sentence_data = correct_tests_sentences + false_tests_sentences
expected_results = [True for _ in range(len(correct_tests_sentences))] + [False for _ in range(len(false_tests_sentences))]
