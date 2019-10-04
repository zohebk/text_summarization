from gensim.summarization import summarize


class MultiLanguageSummarizer:
    def __init__(self):
        pass

    def summarize_text(self,text):
        return summarize(text)


japanese_text = """
デモが続く香港の林鄭月娥（キャリー･ラム）行政長官は4日、デモ参加者のマスクや覆面の着用を禁止すると発表した。植民地時代の緊急状況規則条例（緊急条例）を発動したもの。
香港では6月から反政府・民主化デモが続いている。参加者はマスクや覆面などで顔を覆い、身元の特定を防いでいる。
中国建国70周年に当たる1日には各地で警察との衝突があり、双方に多数のけが人が出ていた。
「悪化を放っておけない」
林鄭行政長官は、こうした暴力が「香港の街を破壊」していると主張。当局は「悪化し続ける状況を放っておくことはできない」と述べた。
緊急条例の発動により、立法会（議会）の手続きを飛ばし、「覆面禁止法」を制定。5日午前0時に発効する。
しかし、実際に従わせるのは難しく、非常に物議をかもすものだという見方が出ている。
禁止法が発表された4日午後には、すでに活動家らが、これに反対するデモ行進を敢行。政府への抗議としてマスクを着用するよう呼びかけている。
＜関連記事＞
香港で抗議参加者が実弾で撃たれる、デモ開始から初めて
香港デモ、外国人記者が警察のゴム弾で片目失明
【香港デモ】 富裕層が「ゴールデン・ビザ」取得　海外移住視野に
何が禁止される？
香港保安局の李家超局長は、覆面禁止法が適用されるのは、デモ行進などの認可および非認可の集会、そして非合法の集会や暴動だと説明した。
マスクや覆面などを顔を覆えるもの全てが禁止の対象となる。フェイスペイントも含まれるという。
一方、健康や職務上の理由でマスクなどの着用が必要な人は除外されるとしている。
緊急状況規則条例とは
緊急状況規則条例では、行政長官が公共の利益のために必要だと判断した場合、議会の承認なしに規制を制定できる。
香港がイギリスの植民地だった1922年に制定されたもので、1967年の暴動鎮圧の際に使われたのを最後に発動されていなかった。
林鄭行政長官は、この禁止法によって香港が非常事態宣言を発令したわけではないと強調。しかし、「香港は深刻な公共の危機にある」と話した。
"""
chinese_text = """香港行政长官林郑月娥宣布，引用《紧急情况规例条例》的授权，制定《禁止蒙面规例》（又称”禁蒙面法“），禁止示威者在公众活动中隐藏脸容，认为这样有效阻吓激进违法行为。
“反送中”示威者不满有关条例，号召民众戴口罩和蒙脸再度上街抗议。香港政府以安全为由，允许公务员在4日下午三时半提早离开政府总部，BBC中文得悉多间公司亦以安全理由呼吁员工尽早放工。晚上在伊利沙伯体育馆举行的国庆活动亦告取消。
多名政客及学者对BBC中文表示，条例未必有成效，反而可能激发群众不满而适得其反。
“禁蒙面法”：遏止香港示威浪潮的灵丹妙药还是火上浇油
香港警方：“我们正被推向极限”
用港英法律打“反送中” 香港“紧急法”从哪里来
政府推动法例的理据
《禁止蒙面规例》从10月5日起实施，订明任何人参与合法或非法的公众活动，都不得使用阻止识辨身分的蒙面物品，违例人士最高被判监1年及罚款2.5万港元。
有关法例容许警方截停和要求蒙面人士移除蒙面用品，如有关人士拒绝警方要求，同样属于犯罪行为。
香港政府说， 规例的目的是保障公共安全秩序，防止暴力行为，阻止暴力人士隐藏身份逍遥法外。
林郑月娥强调，引用规例并不代表香港进入紧急状况，但认为香港目前的情况符合《紧急情况规例条例》中“危害公安”的情况，政府考虑到近四个月以来的示威暴力升级，经过考虑后采取的“合理措施”，希望暴力行为慢慢减退。
至于未来会否再引用《紧急情况规例条例》，是否禁止市民使用Telegram等加密通讯软件，林郑月娥表示，香港政府引用条例的权力并非无上，但如果暴力行为再升级，政府必须继续寻找适当方法和手段应对。
林郑月娥指出，根据《紧急情况规例条例》，行政长官可以废除按条例作出的命令，以往引用规例时亦有废除安排，不过她无法为废除定立期限。
她说，订立《禁止蒙面规例》主要是为了协助警察执法，达致阻吓作用，目前无法预计定立反蒙面法的效果，也并无下一步行动，如果暴力行为再增加，亦会考虑其他行动，但这些行动正在内部评估，暂无法对外透露。
香港律政司长郑若骅表示，《禁止蒙面规例》订立时已充份顾及《基本法》及《人权法》，以合理相称原则，平衡社会利益及市民权利限制，市民仍然可以自由参加合法和平的公众活动，也可在有“合理辩解”下蒙面。宗教、健康或是从事专业需要作出相关行为可被视为“合理辩解”。
香港教育局向全港学校发信，要求除宗教、健康理由外，学生、教职员在校内外也不应戴上口罩或以任何方式遮盖脸孔。
林郑月娥又指，在事件中被捕学生的比例，由6至8月的25%，上升至9月开学后的38%，担心暴力会将青年及香港的未来置于危险境地，因此政府要尽一切努力，阻止学生以身试法，挽救香港未来。
建制派多名政客对法例表示支持，认为有助减少暴力事件。属于香港最大建制派政党民建联的行政会议成员叶国谦说，香港是法治社会，所有人应该守法。他表示，已经不能接受现时社会的暴力行为，《禁止蒙面规例》有助制裁违法人士。
"""
nepali_text = """
निर्माण सम्पन्न भएपछि देशका कार्यकारी प्रमुखले उ‌द्घाटन गरेका त्यस्ता निर्मित संरचना नियमित काममा आउँछन् भन्ने सर्वसाधारणलाई लागेको हुन्छ।
कार्यकारी प्रमुखले उ‌द्घाटन गरेको मात्र नभई सम्पन्न भएका विकासका संरचना सञ्चालनमा आउनै पर्छ।
नेपालमा भने त्यस्ता धेरै संरचना छन् जहाँ प्रधानमन्त्री केपी शर्मा ओलीलाई लगेर उ‌द्घाटन गराइएका छन् तर काममा भने करिब एक वर्ष पुग्न लाग्दा पनि आउन सकेका छैनन्।
प्रधानमन्त्री ओलीले उ‌द्घाटन गरेका तर काममा नआएका विकासका कामहरूः १. काठमाण्डूमा उ‌द्घाटन गरिएका बिजुली बस
गत वर्ष कार्तिक ६ गते लुम्बिनीमा सञ्चालन गर्नका लागि भनेर ल्याइएका बिजुली बसको उ‌द्घाटन प्रधानमन्त्री केपी शर्मा ओलीले गरेका थिए।
उनले ‌उ्दघाटन मात्र गरेनन् त्यही बसमा चढेर सिंहदरबारको यात्रा पनि गरेका थिए।
तर तिनै बस अहिले थन्किएर बसेका छन्।
ती बस एशियाली विकास ब्याङ्कको सहयोगमा खरिद गरिएका हुन्।
पर्यटन मन्त्रालयका अनुसार ती बस गुणस्तरीय छैनन्।
मन्त्रालयका उपसचिव गोपीचन्द्र भण्डारीका अनुसार बसका पार्टपुर्जा र 'बडी' फरक/फरक देशमा बनेको पाइएकोले ती बस सञ्चालन गर्ने पक्षमा मन्त्रालय छैन।
उनले भने, 'हामी बस नै फिर्ता लगेर अरू गुणस्तरका बस ल्याउनुपर्छ भन्दा ठेकेदारले मर्मत गरिदिन्छु भनेकाले कुरा मिलेको छैन।'
मन्त्रालयले खोजेको गुणस्तरका बस ल्याउन नसकेको अवस्था ठेक्का तोड्ने मनस्थितिमा मन्त्रालय पुगेको बताइएको छ।
मन्त्रालयका अनुसार अहिले त्यस्ता पाँचवटा बस ग्यारेजमा थन्किएका छन्।
मन्लालयले खोजेको गुणस्तरको बसको मूल्य करिब डेढ करोड नेपाली रुपैयाँ पर्ने मन्त्रालयका उपसचिव भण्डारीले बताए।
२. विराटनगर नजिकको कृषि बजार
विराटनगरनजिक कटहरी गाउँपालिका १ मा बनेको कृषि बजार प्रधानमन्त्री केपी शर्मा ओलीले गत चैत ३ गते उ‌द्घाटन गरेका थिए।
उनले उ‌द्घाटन गरेको ६ महिना बितिसक्दा पनि उक्त बजार सञ्चालनमा आएको छैन।
स्थानीय जनप्रिय माध्यमिक विद्यालयको ५ बिघा २ धुर जग्गामा १३ करोड ७६ लाख ५४ हजार ७ सय १० रुपैयाँ लागतमा उक्त बजार निर्माण भएको हो।
कटहरी गाउँपालिका कार्यालयका अनुसार उक्त बजार कस्ले सञ्चालन गर्ने भन्ने विषय नै टुङ्गो लागेको छैन।
गाउँपालिकाकी उपप्रमुख मन्जिताकुमारी सरदारले निर्माण गर्ने कम्पनीले जिम्मा नलगाएका कारण उक्त बजार उ‌द्घाटन भए पनि प्रयोगमा आउन नसकेको बताइन्।
उनले भनिन्, 'अहिले त त्यो विषयमा चर्चा पनि छैन।'३. विराटनगरको बायोग्यास प्लान्ट
गत साल भदौ ५ गते विराटनगरको श्रीकृष्ण गौशालाले निर्माण गरेको बायोग्यास प्लान्ट उ‌द्घाटन गर्दा प्रधानमन्त्री ओलीले भनेका थिए, 'अब घर/घरमा पाइपबाट ग्यास।'
उनले उक्त बायोग्यास प्लान्ट उ‌द्घाटन गरेपछि अन्य कुनै पनि घरमा ग्यास जडान भएको छैन।
उ‌द्घाटनका बेला ३२ घरमा उक्त प्लान्टबाट ग्यास जडान गरिएको थियो।
अहिले पनि त्यति नै रहेको गौशालाका अध्यक्ष शङ्करलाल अग्रवालले बताए।
उनले भने, 'हामीले जे सोचेर बायोग्यास उ‌द्घाटन प्रधानमन्त्री ओलीबाट गरायौँ। सो अनुसारको काम अगाडि बढेन। जहाँ थियो त्यहीँ छ। हाम्रो क्षमता चाहिँ करिब ७० घरधुरीको हो।'
अग्रवालले सर्वसाधारणले चासो नदिएकाले पनि ग्यास वितरणको प्रक्रिया अगाडि बढ्न नसकेको बताए।
४. भद्रपुरमा बनेको मेची पुल
भारतको पश्चिम बङ्गाल र बिहार तथा पूर्वी दक्षिण झापा जोड्ने भद्रपुरमा मेची नदीमा बनेको पुल गत माघ १७ गते प्रधानमन्त्री केपी शर्मा ओलीले उद्घाटन गरे पनि अहिलेसम्म उक्त पुलमा सवारी सञ्चालन हुन सकेको छैन।
बाइक, टेम्पो तथा हल्का सवारी साधन सञ्चालन भए पनि अन्य ठूला यात्रु तथा मालवाहक सवारी साधन सञ्चालन भएका छैनन्।
३५ करोड ९५ लाख रुपैयाँको लागतमा नौ वर्षमा उक्त पुल बनेको हो।
भारतीय पक्षले पुल जोड्ने करिब ४०० मिटर सडक नबनेको र नेपालतर्फ बन्ने सडकमा मुआब्जा विवाद रहेको जिल्ला समन्वय समिति झापाका प्रमुख सोमनाथ पोर्तेलले बताए।
उनले भने, 'यस्ता संरचना बन्नलाई धेरै वर्ष लाग्ने गर्छ। त्यसबीचमा बाटो बनाउन सकिन्थ्यो। हाम्रै अदूरदर्शिताका कारण समस्या भयो। प्रधानमन्त्रीले उद्घाटन गर्नुभयो तर सञ्चालन गर्न सकिएन।'

"""
english_text = """
The contribution of cloud computing and mobile computing technologies lead to the newly emerging mobile cloud com- puting paradigm. Three major approaches have been pro- posed for mobile cloud applications: 1) extending the access to cloud services to mobile devices; 2) enabling mobile de- vices to work collaboratively as cloud resource providers; 3) augmenting the execution of mobile applications on portable devices using cloud resources. In this paper, we focus on the third approach in supporting mobile data stream applica- tions. More specifically, we study how to optimize the com- putation partitioning of a data stream application between mobile and cloud to achieve maximum speed/throughput in processing the streaming data. To the best of our knowledge, it is the first work to study the partitioning problem for mobile data stream applica- tions, where the optimization is placed on achieving high throughput of processing the streaming data rather than minimizing the makespan of executions as in other appli- cations. We first propose a framework to provide runtime support for the dynamic computation partitioning and exe- cution of the application. Different from existing works, the framework not only allows the dynamic partitioning for a single user but also supports the sharing of computation in- stances among multiple users in the cloud to achieve efficient utilization of the underlying cloud resources. Meanwhile, the framework has better scalability because it is designed on the elastic cloud fabrics. Based on the framework, we design a genetic algorithm for optimal computation parti- tion. Both numerical evaluation and real world experiment have been performed, and the results show that the par- titioned application can achieve at least two times better performance in terms of throughput than the application without partitioning.
"""
hindi_text = """
एक कहावत है 'खोदा पहाड़ निकली चुहिया.' 'साहो' देखने गए लोगों का फ़िल्म देखने के बाद इस कहावत से राब्ता हो सकता है.
बाहुबली फ़िल्म के बाद अभिनेता प्रभास की धमाकेदार एंट्री की उम्मीद लेते हुए जब हम 'साहो' देखने पहुंचे तो केवल मायूसी ही हाथ लगी.
ये फ़िल्म चार भाषाओं में एक साथ रिलीज़ हुई है. ज़ाहिर है प्रभास के इतने फैन्स हैं कि हर शहर में लोगों ने पहले ही इस फ़िल्म की बुकिंग करा रखी थी.
'बाहुबली' के बाद कुछ लोगों को इंतज़ार था कि इतने बड़े पैमाने की फ़िल्म के बाद ये फ़िल्म भी बॉक्स ऑफिस पर खरी उतरेगी.
ऐसा नहीं है कि फ़िल्म में वैसा मसाला नहीं है जो इस तरह की फ़िल्म में होना चाहिए. फ़िल्म में साथी कलाकार के रूप में जैकी श्रॉफ, टीनू आनंद, चंकी पांडे, मंदिरा बेदी, अरुण विजय, प्रकाश बेलावाडी जैसे कई मंझे हुए कलाकार हैं. पर उनके पास फ़िल्म में कुछ ख़ास करने के लिए नहीं है.
एक तरह से देखा जाए तो ये सब केवल कुछ पात्रों को भरने के लिए ही रखे गए हैं.
फ़िल्म एक काल्पनिक शहर वाजीपुर से शुरू होती है. जहां पर जैकी श्रॉफ रॉय नाम का अंपायर चलाते हैं. वो काला धंधा करते हैं और उनकी शाखाएं देश-विदेश में फैली हुई हैं. पर कुछ इज़्जत कमाने के लिए वो स्टील की एक फैक्ट्री लगाना चाहते हैं जिसके लिए उनको कुछ राजनीतिज्ञों की मदद की ज़रूरत पड़ती है.
उनके दल के कुछ सदस्य ऐसे हैं जो उनसे बदला लेना चाहते हैं. इस रंजिश में जैकी श्रॉफ की हत्या हो जाती है. इसके बाद कहानी कई देशों में घूमती है. जहां चीन, अफ्रीका और कुछ भारत के लोग भी शामिल हैं.
दूसरी ओर बंबई में कुछ पुलिस अफसर हैं जो रॉय अंपायर के फैले धंधे से परेशान हैं. इनमें शामिल हैं मुरली, श्रद्धा कपूर और प्रभास.
जब प्रभास ठान लेते हैं कि वो रॉय अंपायर का खात्मा कर देंगे तब शुरू होती है लड़ाई पुलिस और अंडरवर्ल्ड की. रॉय अंपायर एक ब्लैकबॉक्स की तलाश में होता है जिसके खुलने से उनके हाथ बहुत-सी पूंजी लगेगी. लेकिन इस ब्लैकबॉक्स के बारे में पुलिस को पहले से ही पता होता है.
प्रभास: मैं हिन्दी में लिखता और पढ़ता हूँ
विद्या बालन ने क्यों कहा- वो ख़ुद को धार्मिक नहीं बताना चाहतीं
इसके बाद फ़िल्म की कहानी रुक जाती है और चूहे-बिल्ली के खेल की तरह पुलिस और अंडरवर्ल्ड के बीच तनाव शुरू हो जाता है. इसके अलावा प्लॉट के नाम पर फ़िल्म शून्य है.
हालांकि फ़िल्म की गति तो तेज़ हो जाती है लेकिन उस दौरान हम सिर्फ़ तमाम गाड़ियां उड़ते हुए देखते हैं और बहुत तेज़ एक्शन के चलते कुछ किरदारों को आते-जाते देखते हैं. इसी बीच फ़िल्म में दो-तीन गाने और नाच ठूंसा गया है.
ज़ाहिर है कि प्रभास के साथ श्रद्धा कपूर का रोमांस फिल्म में जोड़ना ज़रूरी था. इसी दौरान हमें नील नितिन मुकेश भी नज़र आते हैं जिनको लेकर ये संशय बना रहता है कि वो पुलिस के आदमी हैं या अंडरवर्ल्ड के.
प्रभास पूरी फ़िल्म में छाए रहते हैं और कुछ सस्पेंस रखते हुए हमें ये भी नहीं पता चल पाता कि वो पुलिस में हैं भी या नहीं. ऐसे कई सीन हैं जहां डायलॉग की कमी खलती है.
शायद उनकी हिंदी इतनी अच्छी नहीं है इसी वजह से वो एक्शन करते हुए ज़्यादा नज़र आते हैं.
फ़िल्म में सीजीआई (कंप्यूटर जेनरेटेड इमेज़री) के ज़रिए कुछ रोमांच से भरे दृश्य ज़रूर हैं जो वास्तविकता से बहुत दूर हैं और केवल दर्शकों को खुश करने के लिए रखे गए हैं.
तकनीकी दृष्टि से देखा जाए तो ये सीन किसी भी हॉलीवुड फ़िल्म की टक्कर के हैं. कमी है तो सिर्फ़ एक कहानी की. क्योंकि केवल एक्शन के बल पर तीन घंटे फ़िल्म को झेलना मुश्किल हो जाता है.
प्रभास को एक लोकप्रिय बॉलीवुड निर्देशक की फ़िल्म से शुरुआत करनी चाहिए थी. लेकिन शायद बाहुबली का प्रभाव इतना अधिक है कि वो उसी में अपने आप को ढाले हुए हैं. कुछ सलमान और अक्षय कुमार की फ़िल्मों का भी असर होगा.
इसके अलावा उत्तर भारत में अपना रंग जमाने के उद्देश्य से ही उन्होंने ऐसी फ़िल्म का चयन किया है जिसमें केवल उनके सिक्स पैक्स एब्स, एक लाइन की कहानी, तीन गाने और बहुत सारा एक्शन ही फ़िल्म में मौजूद है. फ़िल्म देखने के बाद बस एक ही बात दिल से निकलती है कि काश फ़िल्म में एक प्लॉट भी होता.
"""

t = MultiLanguageSummarizer()

eng_summary = t.summarize_text(english_text)
print(eng_summary)
print("====="*20)
hindi_summary = t.summarize_text(hindi_text)
print(hindi_summary)
print("====="*20)
japanese_text_summary = t.summarize_text(japanese_text)
print(japanese_text_summary)
print("====="*20)
chinese_summary = t.summarize_text(chinese_text)
print(chinese_summary)
print("====="*20)
nepali_summary = t.summarize_text(nepali_text)
print(nepali_summary)
print("====="*20)

