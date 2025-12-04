# import streamlit as st

# # Sahifa sozlamalari
# st.set_page_config(
#     page_title="BQD Taqdimoti",
#     page_icon="📋",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # CSS stillari
# st.markdown("""
# <style>
#     .main-title {
#         font-size: 2.5rem;
#         font-weight: bold;
#         color: #1e40af;
#         text-align: center;
#         margin-bottom: 1rem;
#     }
#     .subtitle {
#         font-size: 1.2rem;
#         color: #64748b;
#         text-align: center;
#         margin-bottom: 2rem;
#     }
#     .info-box {
#         padding: 1.5rem;
#         border-radius: 0.5rem;
#         margin-bottom: 1rem;
#     }
#     .blue-box {
#         background-color: #eff6ff;
#         border-left: 4px solid #3b82f6;
#     }
#     .green-box {
#         background-color: #f0fdf4;
#         border-left: 4px solid #22c55e;
#     }
#     .purple-box {
#         background-color: #faf5ff;
#         border-left: 4px solid #a855f7;
#     }
#     .orange-box {
#         background-color: #fff7ed;
#         border-left: 4px solid #f97316;
#     }
#     .red-box {
#         background-color: #fef2f2;
#         border-left: 4px solid #ef4444;
#     }
#     .yellow-box {
#         background-color: #fefce8;
#         border-left: 4px solid #eab308;
#     }
#     .section-title {
#         font-size: 1.3rem;
#         font-weight: bold;
#         margin-bottom: 1rem;
#     }
#     .formula {
#         font-family: monospace;
#         font-size: 1.1rem;
#         text-align: center;
#         padding: 1rem;
#         background-color: #f8fafc;
#         border-radius: 0.5rem;
#     }
# </style>
# """, unsafe_allow_html=True)

# # Sidebar navigatsiya
# st.sidebar.title("📑 Taqdimot Bo'limlari")
# st.sidebar.markdown("---")

# slides = [
#     "🏠 Kirish",
#     "📊 BQD Turlari",
#     "💻 Taqdim Shakllari",
#     "📝 BQD-1 To'ldirish",
#     "⚠️ Muhim Grafalari",
#     "📋 BQD-2 To'ldirish",
#     "📎 Hujjatlar",
#     "⚡ Eslatmalar",
#     "✅ Xulosa"
# ]

# current_slide = st.sidebar.radio("Bo'limni tanlang:", slides, index=0)

# # Asosiy kontent
# if current_slide == "🏠 Kirish":
#     st.markdown('<p class="main-title">📋 Bojxona Qiymat Deklaratsiyasi (BQD)</p>', unsafe_allow_html=True)
#     st.markdown('<p class="subtitle">O\'zbekiston Respublikasi bojxona hududiga olib kiriladigan tovarlar uchun</p>', unsafe_allow_html=True)
    
#     st.markdown('<div class="info-box blue-box">', unsafe_allow_html=True)
#     st.markdown("### 📖 Asosiy Ta'rif")
#     st.write("""
#     **BQD** — bojxona yuk deklaratsiyasining (BYD) ajralmas qismi bo'lib, 
#     tovarning bojxona qiymati to'g'risidagi ma'lumotlar ko'rsatilgan va 
#     deklarant yoki bojxona brokeri tomonidan bojxona organiga BYD bilan 
#     bir paytda topshiriladigan hujjat.
#     """)
#     st.markdown('</div>', unsafe_allow_html=True)
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
#         st.markdown("#### 📄 BQD-1")
#         st.write("1-usul (bitim qiymati) uchun")
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with col2:
#         st.markdown('<div class="info-box purple-box">', unsafe_allow_html=True)
#         st.markdown("#### 📋 BQD-2")
#         st.write("2-6 usullar uchun")
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     st.info("ℹ️ BQD Bojxona kodeksining 303-313-moddalariga muvofiq to'ldiriladi")

# elif current_slide == "📊 BQD Turlari":
#     st.markdown('<p class="main-title">📊 BQD Turlari va Qo\'llanilishi</p>', unsafe_allow_html=True)
    
#     st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
#     st.markdown("### ✅ BQD-1 (1-usul)")
#     st.write("**Olib kiriladigan tovarga doir bitimning qiymatiga oid usul**")
#     st.markdown("""
#     - ✓ Sotuvchi va sotib oluvchi o'rtasida to'g'ridan-to'g'ri sotish-sotib olish bitimi mavjud
#     - ✓ Bitim narxi aniq va hujjat bilan tasdiqlangan
#     - ✓ Eng keng qo'llaniladigan usul
#     - ✓ 90% dan ortiq holatlarda ishlatiladi
#     """)
#     st.markdown('</div>', unsafe_allow_html=True)
    
#     st.markdown('<div class="info-box purple-box">', unsafe_allow_html=True)
#     st.markdown("### 🔄 BQD-2 (2-6 usullar)")
#     st.write("**1-usulni qo'llab bo'lmaganda qo'llaniladigan alternativ usullar**")
    
#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown("""
#         **2-usul:** Aynan bir xil tovar bitimi  
#         **3-usul:** O'xshash tovar bitimi  
#         **4-usul:** Qiymatlarni chegirish usuli
#         """)
#     with col2:
#         st.markdown("""
#         **5-usul:** Qiymatlarni qo'shish usuli  
#         **6-usul:** Zaxira usul (1-5 asosida)
#         """)
#     st.markdown('</div>', unsafe_allow_html=True)

# elif current_slide == "💻 Taqdim Shakllari":
#     st.markdown('<p class="main-title">💻 BQD Taqdim Etish Shakllari</p>', unsafe_allow_html=True)
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown('<div class="info-box blue-box">', unsafe_allow_html=True)
#         st.markdown("### 📱 Elektron shakl")
#         st.markdown("""
#         ✅ TEDAAT tizimi orqali  
#         ✅ Elektron raqamli imzo (ERI) bilan  
#         ✅ BYD elektron bo'lsa, BQD ham elektron  
#         ✅ Tezkor va qulay
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with col2:
#         st.markdown('<div class="info-box orange-box">', unsafe_allow_html=True)
#         st.markdown("### 📄 Qog'oz shakl")
#         st.markdown("""
#         ✅ A4 formatda 4 nusxada  
#         ✅ Elektron nusxasi ERI bilan  
#         ✅ Imzo va muhur zarur
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
#     st.markdown("### 📑 Nusxalar Taqsimoti (Qog'oz shakl)")
#     st.markdown("""
#     1. **1-nusxa:** Bojxona organlari uchun (arxivda saqlanadi)
#     2. **2-nusxa:** Deklaratsiyalovchi shaxs uchun
#     3. **3-4 nusxalar:** Deklarant uchun
#     """)
#     st.markdown('</div>', unsafe_allow_html=True)

# elif current_slide == "📝 BQD-1 To'ldirish":
#     st.markdown('<p class="main-title">📝 BQD-1 To\'ldirish Tartibi</p>', unsafe_allow_html=True)
#     st.markdown('<p class="subtitle">Asosiy grafalar va ularning mazmuni</p>', unsafe_allow_html=True)
    
#     with st.expander("🔵 A BO'LIM: Hisoblash uchun asos", expanded=True):
#         st.markdown("""
#         **11a-grafa:** Bitim narxi
#         - 1-qator: Kontrakt valyutasida
#         - 2-qator: Milliy valyutada
#         - 3-qator: Valyuta kursi
        
#         **11b-grafa:** Bilvosita to'lovlar summasi
#         - Sotuvchi manfaati uchun uchinchi shaxslarga to'lovlar
#         - Bitim narxiga tuzatishlar
        
#         **12-grafa:** Jami = 11a + 11b
#         """)
    
#     with st.expander("🟢 B BO'LIM: Qo'shimcha hisoblar"):
#         col1, col2 = st.columns(2)
#         with col1:
#             st.markdown("""
#             **13a:** Vositachilik haqlari  
#             **13b:** Konteyner va o'rov-joylov  
#             **14:** Xomashyo, materiallar  
#             **15:** Litsenziya to'lovlari
#             """)
#         with col2:
#             st.markdown("""
#             **16:** Qayta sotishdan tushum  
#             **17a:** Tashish xarajatlari  
#             **17b:** Yuklash/tushirish  
#             **17v:** Sug'urta
#             """)
#         st.markdown("**18-grafa:** B bo'lim yig'indisi")
    
#     with st.expander("🔴 V BO'LIM: Chegirmalar"):
#         st.markdown("""
#         **19-grafa:** Qurilish, montaj xarajatlari (O'zbekistonda)  
#         **20-grafa:** O'zbekiston ichida tashish  
#         **21-grafa:** Bojxona va boshqa to'lovlar  
#         **22-grafa:** V bo'lim yig'indisi
#         """)
    
#     st.markdown('<div class="info-box purple-box">', unsafe_allow_html=True)
#     st.markdown("### 🧮 Yakuniy Hisob-kitob")
#     st.markdown('<p class="formula"><strong>BOJXONA QIYMATI = (12 + 18) - 22</strong></p>', unsafe_allow_html=True)
#     st.markdown("Bu qiymat **23a-grafa**da ko'rsatiladi va bojxona to'lovlarini hisoblash uchun asos bo'ladi.")
#     st.markdown('</div>', unsafe_allow_html=True)

# elif current_slide == "⚠️ Muhim Grafalari":
#     st.markdown('<p class="main-title">⚠️ BQD-1: Muhim va Tanqidiy Grafalari</p>', unsafe_allow_html=True)
    
#     st.markdown('<div class="info-box yellow-box">', unsafe_allow_html=True)
#     st.markdown("### ❓ 7a-7b grafalar: O'zaro bog'liqlik")
#     st.write("**Savol:** Sotuvchi va sotib oluvchi o'rtasida o'zaro bog'liqlik mavjudmi?")
#     st.warning("""
#     ⚠️ Agar "Ha" javob berilsa va bog'liqlik bitim narxiga ta'sir qilgan bo'lsa:
#     - 1-usul qo'llanilmaydi
#     - BQD-2 to'ldirilishi kerak
#     - 2-6 usullardan biri tanlanadi
#     """)
#     st.markdown('</div>', unsafe_allow_html=True)
    
#     st.markdown('<div class="info-box red-box">', unsafe_allow_html=True)
#     st.markdown("### 🚫 8a-8b grafalar: Shartlar va cheklovlar")
#     st.write("**Savol:** Sotish yoki bitimning bahosiga cheklovlar bormi?")
#     st.error("""
#     🛑 Quyidagi hollarda 1-usul qo'llanilmaydi:
#     - Shartlarni miqdoriy baholash mumkin emas
#     - Tovarni qaytarish talablari mavjud
#     - Narxga ta'sir etuvchi aniqlanmagan omillar bor
#     """)
#     st.markdown('</div>', unsafe_allow_html=True)
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown('<div class="info-box blue-box">', unsafe_allow_html=True)
#         st.markdown("### 💡 9a-grafa")
#         st.write("**Intellektual mulk to'lovlari**")
#         st.markdown("""
#         - Litsenziya to'lovlari
#         - Mualliflik haqi
#         - Patent to'lovlari
#         - Tovar belgisi uchun
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with col2:
#         st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
#         st.markdown("### 💰 9b-grafa")
#         st.write("**Qayta sotishdan tushum**")
#         st.markdown("""
#         - Sotuvchiga tegishli ulush
#         - Daromadning foizi
#         - Keyingi sotishdan foyda
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
#     st.markdown("### 🚚 3-grafa: Yetkazib berish shartlari (INCOTERMS)")
    
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.info("**EXW** - Zavod narxi")
#         st.info("**FCA** - Tashuvchiga topshirish")
#     with col2:
#         st.success("**FOB** - Bortda erkin")
#         st.success("**CFR** - Narx + navlun")
#     with col3:
#         st.warning("**CIF** - Narx + sug'urta + navlun")
#         st.warning("**CIP** - Navlun to'langan")
    
#     st.markdown('</div>', unsafe_allow_html=True)

# elif current_slide == "📋 BQD-2 To'ldirish":
#     st.markdown('<p class="main-title">📋 BQD-2 To\'ldirish Tartibi</p>', unsafe_allow_html=True)
#     st.markdown('<p class="subtitle">2-6 usullar uchun maxsus shakl</p>', unsafe_allow_html=True)
    
#     st.markdown('<div class="info-box purple-box">', unsafe_allow_html=True)
#     st.markdown("### 📄 Asosiy Varaq (Barcha usullar uchun)")
#     st.markdown("""
#     **6-grafa:** Qo'llaniladigan usulga "X" belgisi  
#     **7-grafa:** Oldingi usullarni qo'llab bo'lmaslik sabablari (majburiy)  
#     **8-grafa:** Taqdim etilgan asosiy hujjatlar ro'yxati  
#     **9-grafa:** Qo'shimcha varaqlar soni  
#     **10-grafa:** Joy, sana va imzo
#     """)
#     st.markdown('</div>', unsafe_allow_html=True)
    
#     tab1, tab2, tab3, tab4 = st.tabs(["2-usul", "3-usul", "4-usul", "5-usul"])
    
#     with tab1:
#         st.markdown('<div class="info-box blue-box">', unsafe_allow_html=True)
#         st.markdown("### 🔵 2-usul: Aynan bir xil tovar")
#         st.markdown("""
#         **11-grafa:** Aynan bir xil tovarga doir bitim qiymati
#         - So'nggi 90 kun ichida olib kirilgan
#         - Bojxona organi tomonidan qabul qilingan
#         - 1-usul bo'yicha aniqlangan
        
#         **B bo'lim (12a-15):** Tuzatishlar
#         - Miqdor farqi (12a, 14a)
#         - Tijorat shartlari (12b, 14b)
#         - Tashish xarajatlari (12v, 14v)
#         - Yuklash/tushirish (12g, 14g)
#         - Sug'urta (12d, 14d)
        
#         **16-grafa:** Tuzatilgan bitim qiymati  
#         **18a-grafa:** Bojxona qiymati = (16 × 17b) ÷ 17a  
#         **20-grafa:** Ma'lumot manbai (BYD raqami)
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with tab2:
#         st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
#         st.markdown("### 🟢 3-usul: O'xshash tovar")
#         st.write("**2-usul bilan bir xil tartibda, lekin:**")
#         st.markdown("""
#         - Aynan bir xil o'rniga o'xshash tovar ishlatiladi
#         - Tovar xususiyatlari, sifati va obro'si o'xshash bo'lishi kerak
#         - Bir xil mamlakat ishlab chiqaruvchisidan
#         - Grafalarni to'ldirish 2-usul kabi
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with tab3:
#         st.markdown('<div class="info-box orange-box">', unsafe_allow_html=True)
#         st.markdown("### 🟠 4-usul: Qiymatlarni chegirish")
#         st.markdown("""
#         **11-grafa:** O'zbekistonda sotilgan tovar birligi narxi
#         - So'nggi 90 kun ichida sotilgan
#         - Dastlabki holatda (ishlov berilmagan)
        
#         **B bo'lim (12-16):** Chegirib tashlanadi:
#         - **12:** Vositachilik haqi va umumiy xarajatlar
#         - **13:** Bojxona to'lovlari va soliqlar
#         - **14:** Transport xarajatlari O'zbekistonda
#         - **15:** Ishlov berish qiymati (agar mavjud)
        
#         **18a-grafa:** (11 - 16) × 17 = Bojxona qiymati
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with tab4:
#         st.markdown('<div class="info-box red-box">', unsafe_allow_html=True)
#         st.markdown("### 🔴 5-usul: Qiymatlarni qo'shish (Hisoblangan qiymat)")
#         st.markdown("""
#         **11-grafa:** Ishlab chiqarish xarajatlari
#         - Xomashyo va materiallar
#         - Ishlab chiqarish jarayoni
#         - O'rash-joylash
        
#         **12-grafa:** Umumiy xarajatlar + foyda
#         - Ishlab chiqaruvchi umumiy xarajatlari
#         - Oddiy darajadagi foyda
        
#         **13-15:** Transport xarajatlari
#         - Tashish (13)
#         - Yuklash/tushirish (14)
#         - Sug'urta (15)
        
#         **16a-grafa:** 11 + 12 + 13 + 14 + 15 = Bojxona qiymati
#         """)
#         st.info("⚠️ Ishlab chiqaruvchining buxgalterlik hisoblari asosida!")
#         st.markdown('</div>', unsafe_allow_html=True)

# elif current_slide == "📎 Hujjatlar":
#     st.markdown('<p class="main-title">📎 Taqdim Etilishi Kerak Hujjatlar</p>', unsafe_allow_html=True)
    
#     tab1, tab2, tab3, tab4 = st.tabs(["1-usul", "2-3 usullar", "4-usul", "5-usul"])
    
#     with tab1:
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.markdown('<div class="info-box blue-box">', unsafe_allow_html=True)
#             st.markdown("### ✅ Majburiy hujjatlar")
#             st.markdown("""
#             1. ✓ Tashqi savdo kontrakti ID raqami (TEDAAT)
#             2. ✓ Hisobvaraq-faktura (invoys)
#             """)
#             st.markdown('</div>', unsafe_allow_html=True)
        
#         with col2:
#             st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
#             st.markdown("### 📋 Qo'shimcha (zarurat bo'yicha)")
#             st.markdown("""
#             - Sug'urta hujjatlari
#             - Tashish shartnomasi
#             - Transport hujjatlari
#             - Vositachilik shartnomasi
#             - Litsenzion kelishuv
#             - Bank to'lov hujjatlari
#             """)
#             st.markdown('</div>', unsafe_allow_html=True)
        
#         st.markdown('<div class="info-box yellow-box">', unsafe_allow_html=True)
#         st.markdown("### ⚠️ Xavf yuqori bo'lganda")
#         st.markdown("""
#         **Qo'shimcha talab qilinadi:**
#         - Jo'natuvchi mamlakat bojxona deklaratsiyasi
#         - Uchinchi shaxslar bilan kontraktlar
#         - To'lov hisoblari
        
#         *Qachon?: Mazkur tovar oxirgi 90 kun ichida olib kirilgan tovardan 
#         sezilarli arzon bo'lganda*
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with tab2:
#         st.markdown('<div class="info-box purple-box">', unsafe_allow_html=True)
#         st.markdown("### 📋 2-3 usullar uchun hujjatlar")
#         st.markdown("""
#         **Majburiy:**
#         1. ✓ Aynan bir xil/o'xshash tovar BYD raqami
#         2. ✓ 1-usulda qabul qilingan bo'lishi kerak
#         3. ✓ So'nggi 90 kun ichida olib kirilgan
        
#         **Tuzatishlar uchun (zarur bo'lsa):**
#         - Tashish xarajatlari tasdigi
#         - Transport farqi hisob-kitobi
#         - Yetkazib berish shartlari farqi
#         """)
#         st.info("💡 Agar farqlar kichik bo'lsa, qo'shimcha hujjatsiz ham mumkin")
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with tab3:
#         st.markdown('<div class="info-box orange-box">', unsafe_allow_html=True)
#         st.markdown("### 📋 4-usul uchun hujjatlar")
#         st.markdown("""
#         **Zaruriy hujjatlar:**
#         1. ✓ O'zbekistonda sotish shartnomasi
#         2. ✓ Ichki sotish invoysi
#         3. ✓ Bojxona to'lovlari to'langanlik hujjati
#         4. ✓ Bank to'lov hujjatlari
#         5. ✓ Xarajatlarni aks ettiruvchi buxgalterlik hujjatlari
        
#         **Qo'shimcha (agar tovar ishlov berilgan bo'lsa):**
#         - Ishlov berish shartnomasi
#         - Ishlov berish uchun hisob (invoys)
#         - Kalkulyatsiya
#         """)
#         st.warning("⚠️ Hujjatlar yo'qligi BYD elektron bazasi yoki muqobil manbalar bilan almashtirilishi mumkin")
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with tab4:
#         st.markdown('<div class="info-box red-box">', unsafe_allow_html=True)
#         st.markdown("### 📋 5-usul uchun hujjatlar")
#         st.markdown("""
#         **Ishlab chiqaruvchidan:**
#         1. ✓ Buxgalterlik tijorat hisoblari
#         2. ✓ Ishlab chiqarish xarajatlari kalkulyatsiyasi
#         3. ✓ Xomashyo va materiallar qiymati
#         4. ✓ Umumiy xarajatlar va foyda ma'lumoti
        
#         **Qo'shimcha:**
#         - Tashish xarajatlari kalkulyatsiyasi
#         - Transport hujjatlari
#         - Sug'urta polisi
#         """)
#         st.error("""
#         🚫 Muhim talablar:
#         - Hujjatlar ishlab chiqargan mamlakatning buxgalterlik standartlariga mos bo'lishi
#         - Ma'lumotlar aniq va miqdoriy aniqlangan bo'lishi
#         - Hujjat bilan tasdiqlanishi shart
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)

# elif current_slide == "⚡ Eslatmalar":
#     st.markdown('<p class="main-title">⚡ Muhim Eslatmalar va Talablar</p>', unsafe_allow_html=True)
    
#     st.markdown('<div class="info-box red-box">', unsafe_allow_html=True)
#     st.markdown("### 🚫 Qat'iy talablar")
#     st.markdown("""
#     - ❌ BQD o'chish va bo'yashsiz bo'lishi kerak
#     - ❌ Tushunarli va aniq yozilishi shart
#     - ❌ Barcha summalar milliy valyutada
#     - ❌ ERI bilan tasdiqlanishi majburiy
#     - ❌ Hujjatlar rus yoki ingliz tilida (boshqa tillarda tarjima bilan)
#     """)
#     st.markdown('</div>', unsafe_allow_html=True)
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown('<div class="info-box yellow-box">', unsafe_allow_html=True)
#         st.markdown("### ⏰ Muddatlar")
#         st.markdown("""
#         - **90 kun:** 2-4 usullar uchun
#         - **180 kun:** Muqobil (agar 90 da yo'q bo'lsa)
#         - **Bir vaqtda:** BYD bilan birga taqdim
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with col2:
#         st.markdown('<div class="info-box blue-box">', unsafe_allow_html=True)
#         st.markdown("### 💱 Valyuta kursi")
#         st.markdown("""
#         - **Markaziy Bank kursi**
#         - **BYD qabul qilingan kungi**
#         - **Qayta hisoblash majburiy**
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     st.markdown('<div class="info-box orange-box">', unsafe_allow_html=True)
#     st.markdown("### 📝 To'ldirish qoidalari")
#     st.markdown("""
#     ✅ **To'g'ri:**
#     - Grafalar ketma-ket to'ldirilishi
#     - Joy yetmasa orqa tomonga yoki qo'shimcha varaqga
#     - Har bir ma'lumot tegishli grafada
#     - Imzo va muhur aniq
    
#     ❌ **Noto'g'ri:**
#     - Grafalarni o'tkazib yuborish
#     - Ma'lumotlarni aralashtirib yuborish
#     - Qo'shimcha varaqsiz bermaslik
#     """)
#     st.markdown('</div>', unsafe_allow_html=True)
    
#     st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
#     st.markdown("### 🔄 Qayta ishlash")
#     st.markdown("""
#     **Agar kamchiliklar aniqlansa:**
#     1. Bojxona organi xabar beradi
#     2. Deklaratsiyalovchi shaxs tuzatadi
#     3. Qayta taqdim etiladi
#     4. Dastlabki tekshiruv o'tkaziladi
    
#     **Qabul qilingandan keyin:**
#     - BQD BYD bilan bir vaqtda rasmiylashtiriladi
#     - BYD raqami BQDga biriktiriladi
#     - Bojxona organi belgilarini qo'yadi
#     """)
#     st.markdown('</div>', unsafe_allow_html=True)

# elif current_slide == "✅ Xulosa":
#     st.markdown('<p class="main-title">✅ Xulosa va Asosiy Xulosalar</p>', unsafe_allow_html=True)
    
#     st.markdown('<div class="info-box blue-box">', unsafe_allow_html=True)
#     st.markdown("### 🎯 BQD ning asosiy maqsadi")
#     st.write("""
#     Bojxona qiymat deklaratsiyasi tovarning bojxona qiymatini to'g'ri va shaffof 
#     aniqlash, bojxona to'lovlarini hisoblash uchun asos yaratish va halqaro 
#     savdo qoidalariga rioya etilishini ta'minlashga xizmat qiladi.
#     """)
#     st.markdown('</div>', unsafe_allow_html=True)
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
#         st.markdown("### ✅ Asosiy qoidalar")
#         st.markdown("""
#         1. **Aniqlik** - barcha ma'lumotlar to'g'ri
#         2. **To'liqlik** - hamma grafalarda ma'lumot
#         3. **Hujjatlilik** - tasdiqlangan hujjatlar
#         4. **Vaqtida** - BYD bilan birga
#         5. **Elektron** - ERI bilan tasdiq
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with col2:
#         st.markdown('<div class="info-box purple-box">', unsafe_allow_html=True)
#         st.markdown("### 📊 Usullar ierarxiyasi")
#         st.markdown("""
#         **1-usul** → Asosiy (90%+)  
#         ⬇️ (qo'llab bo'lmasa)  
#         **2-usul** → Aynan bir xil tovar  
#         ⬇️  
#         **3-usul** → O'xshash tovar  
#         ⬇️  
#         **4-usul** → Ichki sotish narxi  
#         ⬇️  
#         **5-usul** → Hisoblangan qiymat  
#         ⬇️  
#         **6-usul** → Zaxira (yuqoridagilar asosida)
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     st.markdown('<div class="info-box yellow-box">', unsafe_allow_html=True)
#     st.markdown("### 💡 Amaliy maslahatlar")
    
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         st.markdown("""
#         **Tayyorgarlik:**
#         - Hujjatlarni oldindan yig'ing
#         - Kontrakt shartlarini tekshiring
#         - Kurslarga e'tibor bering
#         """)
    
#     with col2:
#         st.markdown("""
#         **To'ldirish:**
#         - Grafalarni ketma-ket to'ldiring
#         - Hisob-kitoblarni tekshiring
#         - Summalarni solishtirib ko'ring
#         """)
    
#     with col3:
#         st.markdown("""
#         **Tekshirish:**
#         - Barcha grafalarda ma'lumot bormi
#         - Hujjatlar to'liqmi
#         - ERI to'g'rimi
#         """)
    
#     st.markdown('</div>', unsafe_allow_html=True)
    
#     st.markdown('<div class="info-box orange-box">', unsafe_allow_html=True)
#     st.markdown("### 📞 Foydali ma'lumotlar")
#     st.markdown("""
#     **Qonunchilik asoslari:**
#     - O'zbekiston Respublikasi Bojxona kodeksi (303-313-moddalar)
#     - "Davlat bojxona xizmati to'g'risida"gi Qonun
#     - Iqtisodiyot va moliya vaziri 298-son buyrugʻi (2025-yil 3-noyabr)
    
#     **Elektron tizimlar:**
#     - TEDAAT (Tovarlarni elektron deklaratsiyalash)
#     - Tashqi savdo operatsiyalarining yagona elektron tizimi
#     - Bojxona organlari elektron bazasi
#     """)
#     st.markdown('</div>', unsafe_allow_html=True)
    
#     st.markdown('<div class="info-box red-box">', unsafe_allow_html=True)
#     st.markdown("### ⚠️ Tez-tez uchraydigan xatolar")
#     st.error("""
#     ❌ 1-usulni noto'g'ri qo'llash (bog'liqlik e'tiborga olinmagan)  
#     ❌ Tuzatishlarni unutish (transport, sug'urta)  
#     ❌ Valyuta kursini noto'g'ri qo'llash  
#     ❌ Hujjatlarning to'liq emasligi  
#     ❌ Grafalarni noto'g'ri to'ldirish  
#     ❌ Elektron va qog'oz nusxalarning farqi
#     """)
#     st.markdown('</div>', unsafe_allow_html=True)
    
#     st.success("""
#     ### 🎓 E'tiboringiz uchun rahmat!
    
#     Savollar bormi? Bojxona organlari yoki vakolatli brokerlar bilan maslahatlashing.
#     """)
    
#     # Qo'shimcha resurslar
#     with st.expander("📚 Qo'shimcha resurslar va havolalar"):
#         st.markdown("""
#         **Rasmiy manbalar:**
#         - [Qonunchilik ma'lumotlari milliy bazasi](https://lex.uz)
#         - [Davlat bojxona qo'mitasi](https://customs.uz)
#         - [Iqtisodiyot va moliya vazirligi](https://mf.uz)
        
#         **Yo'riqnomalar:**
#         - Bojxona yuk deklaratsiyasini to'ldirish tartibi (2773-raqam)
#         - Tovarning bojxona qiymatini aniqlash tartibi (VM 160-son qaror)
#         - TIF TN (Tashqi iqtisodiy faoliyat tovar nomenklaturasi)
        
#         **Tasniflagichlar:**
#         - Valyutalar tasniflagichi
#         - Mamlakatlar tasniflagichi
#         - Yetkazib berish shartlari (INCOTERMS 2020)
#         """)

# # Footer
# st.markdown("---")
# st.markdown("""
# <div style='text-align: center; color: #64748b; padding: 2rem;'>
#     <p><strong>Bojxona qiymat deklaratsiyasi (BQD)</strong></p>
#     <p>O'zbekiston Respublikasi bojxona qonunchiligiga muvofiq</p>
#     <p style='font-size: 0.9rem; margin-top: 1rem;'>
#         📋 Qonunchilik asosi: Bojxona kodeksi, Iqtisodiyot va moliya vaziri 298-son buyrugʻi
#     </p>
#     <p style='font-size: 0.8rem; color: #94a3b8;'>
#         So'nggi yangilanish: 2025-yil noyabr
#     </p>
# </div>
# """, unsafe_allow_html=True)

# # Navigatsiya tugmalari
# st.markdown("---")
# col1, col2, col3 = st.columns([1, 2, 1])

# with col1:
#     current_index = slides.index(current_slide)
#     if current_index > 0:
#         if st.button("⬅️ Oldingi", use_container_width=True):
#             st.session_state.slide = slides[current_index - 1]
#             st.rerun()

# with col2:
#     st.markdown(f"<p style='text-align: center; color: #64748b;'>Sahifa {current_index + 1} / {len(slides)}</p>", unsafe_allow_html=True)

# with col3:
#     if current_index < len(slides) - 1:
#         if st.button("Keyingi ➡️", use_container_width=True):
#             st.session_state.slide = slides[current_index + 1]
#             st.rerun()

# # Qo'llanma bo'limi
# with st.sidebar:
#     st.markdown("---")
#     st.markdown("### 📖 Qo'llanma")
    
#     with st.expander("🔍 BQD turlari"):
#         st.markdown("""
#         **BQD-1:** 1-usul uchun  
#         **BQD-2:** 2-6 usullar uchun
#         """)
    
#     with st.expander("💡 Maslahatlar"):
#         st.markdown("""
#         - Hujjatlarni oldindan tayyorlang
#         - Grafalarni ketma-ket to'ldiring
#         - Hisob-kitoblarni tekshiring
#         - Valyuta kursiga e'tibor bering
#         """)
    
#     with st.expander("⚠️ Ogohlantirishlar"):
#         st.markdown("""
#         - 1-usulni faqat shartlar bajarilganda qo'llang
#         - Barcha hujjatlarni saqlang
#         - Muddatlarga rioya qiling
#         - ERI ni unutmang
#         """)
    
#     st.markdown("---")
#     st.info("💡 Klaviatura bilan navigatsiya: ← → tugmalari")




















# app.py
import streamlit as st
from datetime import datetime

# -----------------------
# Sahifa asosiy sozlamalari
# -----------------------
st.set_page_config(
    page_title="BQD Interaktiv Taqdimot",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------
# CSS: dizaynni chiroyli qilish
# -----------------------
st.markdown(
    """
    <style>
    /* Global */
    .stApp { font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial; }
    .main-header { font-size: 2.4rem; font-weight: 800; color: #0f172a; text-align: center; margin-bottom: 0.25rem; }
    .sub-header { color: #475569; text-align:center; margin-bottom: 1.2rem; font-size:1rem; }
    .card { border-radius: 14px; padding: 18px; box-shadow: 0 6px 20px rgba(2,6,23,0.06); margin-bottom: 12px; background: linear-gradient(180deg, #ffffffef, #fbfdff); }
    .info-title { font-weight:700; font-size:1.05rem; margin-bottom:6px; color:#0f172a; }
    .small-muted { color:#64748b; font-size:0.9rem; }
    .formula { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", monospace; background:#f8fafc; padding:10px;border-radius:8px; text-align:center; }
    .footer { color:#94a3b8; text-align:center; padding:18px; font-size:0.9rem; }
    .graf-label { font-weight:700; color:#0b61ff; }
    .example { font-style:italic; color:#475569; }
    /* Buttons */
    .nav-btn { width:100%; padding:10px 14px; border-radius:10px; border:none; cursor:pointer; font-weight:600; }
    /* Responsive columns */
    @media (max-width: 900px) {
        .stApp .block-container { padding-left:1rem; padding-right:1rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------
# Manbalar (foydalanuvchiga ko'rsatiladi)
# (Webdan olinadigan asosiy yo'riqnomalar / hujjatlar)
# -----------------------
st.sidebar.markdown("### 📚 Manbalar")
st.sidebar.markdown(
    """
- Yo'riqnoma: *Tovarning bojxona qiymatini aniqlash tartibi* (Davlat bojxona qo'mitasi). :contentReference[oaicite:1]{index=1}  
- Bojxona kodeksi (moddalar 303–313). :contentReference[oaicite:2]{index=2}  
- Qo'shimcha qarorlar va 4-usul/6-usul haqida izohlar. :contentReference[oaicite:3]{index=3}
"""
)

# -----------------------
# Sahifa slaydlari (strukturani defolt jadval bilan)
# -----------------------
slides = [
    "🏠 Kirish",
    "📋 BQD haqida qisqacha",
    "📑 Grafalar (1–23) — Toʻliq tushuntirish",
    "💡 Muhim qoidalar va misollar",
    "📎 Hujjatlar va isbotlovchi ma'lumotlar",
    "⚠️ Xatoliklar va tavsiyalar",
    "✅ Xulosa"
]

if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

# Side navigation (radio)
selected = st.sidebar.radio("Bo'lim tanlang:", slides, index=st.session_state.slide_index)
st.session_state.slide_index = slides.index(selected)

# Top header
st.markdown(f"<div class='main-header'>📋 Bojxona Qiymat Deklaratsiyasi — Interaktiv Qo'llanma</div>", unsafe_allow_html=True)
st.markdown(f"<div class='sub-header'>Sizning qo'llanmalaringiz uchun to'liq izoh: grafalar, misollar, hujjatlar va tez-tez uchraydigan xatolar</div>", unsafe_allow_html=True)
st.markdown("---")

# -----------------------
# Helper funksiyalar
# -----------------------
def nav_buttons():
    cols = st.columns([1, 2, 1])
    with cols[0]:
        if st.button("⬅️ Oldingi"):
            idx = st.session_state.slide_index - 1
            if idx >= 0:
                st.session_state.slide_index = idx
                st.experimental_rerun()
    with cols[1]:
        st.write(f"Sahifa {st.session_state.slide_index+1} / {len(slides)}")
    with cols[2]:
        if st.button("Keyingi ➡️"):
            idx = st.session_state.slide_index + 1
            if idx < len(slides):
                st.session_state.slide_index = idx
                st.experimental_rerun()

# -----------------------
# Kontent bo'limlari
# -----------------------
if selected == "🏠 Kirish":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='info-title'>BQD nima va uning ahamiyati</div>", unsafe_allow_html=True)
    st.markdown("""
- BQD (Bojxona qiymat deklaratsiyasi) — bojxona yuk deklaratsiyasining ajralmas qismi bo'lib, tovarning bojxona qiymati haqidagi ma'lumotlarni o'z ichiga oladi. Bu ma'lumot deklarant yoki broker tomonidan BYD bilan birga topshiriladi. :contentReference[oaicite:4]{index=4}
- Bojxona qiymatini aniqlashda xalqaro qoidalar va mahalliy yo'riqnomalar (yo'riqnoma, Vazirlar Mahkamasi qarorlari) asos qilib olinadi. :contentReference[oaicite:5]{index=5}
""")
    st.markdown("<div class='small-muted'>Taqdimot oxirida siz har bir grafa uchun to'liq izoh va qanday hujjatlar kerakligi bilan tanishasiz.</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    nav_buttons()

elif selected == "📋 BQD haqida qisqacha":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='info-title'>Usullar ierarxiyasi (1 → 6)</div>", unsafe_allow_html=True)
    st.markdown("""
1. **1-usul (bitim qiymati)** — asosiy usul, sotuvchi va xaridor o'rtasidagi to'g'ridan-to'g'ri bitim narxi asosida (uyg'un shartlar bilan).  
2. **2-usul (aynan bir xil tovar)** — agar 1-usulni qo'llab bo'lmasa, so'nggi 90 kun ichida olib kirilgan aynan bir xil tovar bitimlari.  
3. **3-usul (o'xshash tovar)** — xususiyatlari va sifati o'xshash tovarlar.  
4. **4-usul (ichki bozor narxi/chegirish)** — mamlakat ichidagi sotish narxi va kerakli tuzatishlar.  
5. **5-usul (qo'shish/hisoblangan qiymat)** — ishlab chiqarish asosida hisoblangan qiymat.  
6. **6-usul (zaxira)** — yuqoridagi usullardan birortasi ishlamagan taqdirda qo'llaniladigan zaxira mexanizmi.  
    """)
    st.markdown("<div class='small-muted'>Mazkur ierarxiya O'zbekiston hududida bojxona qiymatini aniqlashda qo'llaniladigan asosiy tamoyildir. :contentReference[oaicite:6]{index=6}</div>", unsafe_allow_html=True)
    st.markdown("</div> ", unsafe_allow_html=True)

    st.markdown("---")
    nav_buttons()

elif selected == "📑 Grafalar (1–23) — Toʻliq tushuntirish":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='info-title'>Grafalar bo'yicha interaktiv izoh</div>", unsafe_allow_html=True)

    st.markdown("Quyida BQDdagi eng ko'p ishlatiladigan grafalar — har biri uchun: maqsad, talab qilinadigan ma'lumot va misol keltirilgan.")
    st.markdown("**E'tibor:** aniq rasmiy talablarga yo'riqnoma va qarorlarga murojaat qiling. :contentReference[oaicite:7]{index=7}")

    # We'll render each grafa as expander for clarity
    with st.expander("1. Grafa — Tashuvchi/kontrakt raqami va sana", expanded=False):
        st.markdown("**Maqsad:** Kontrakt yoki BYD bilan bog'langan identifikatorni ko'rsatish.")
        st.markdown("**Nima kiritiladi:** Tashqi savdo kontrakti (ID), invoys raqami, sana.")
        st.markdown("**Misol:** `INV-2025-0456, 2025-11-02`")
        st.markdown("**Ogohlantirish:** Sana va raqamlar TEDAAT tizimidagi hujjatlar bilan mos bo'lishi kerak.")

    with st.expander("2. Grafa — Yetkazib berish shartlari (INCOTERMS)", expanded=False):
        st.markdown("**Maqsad:** Tashish shartlari (EXW, FOB, CIF va h.k.) bojxona qiymatini aniqlashda muhim rol o'ynaydi.")
        st.markdown("**Ta'siri:** Masalan, CIF — narxga sug'urta va navlun kiritilgan bo'ladi; EXW — yetkazib berish xarajatlari alohida qo'shilishi kerak.")
        st.markdown("**Qoida:** BYD dagi INCOTERMS bilan BQDdagi 3-grafa mosligini tekshiring. :contentReference[oaicite:8]{index=8}")

    with st.expander("3. Grafa — Bitim qiymati (11a-grafa kabi)", expanded=False):
        st.markdown("**Maqsad:** 1-usul bo'yicha bitim narxini kiritish (kontrakt bo'yicha).")
        st.markdown("**Nima kiritiladi:** Kontrakt narxi valyutada, mahalliy valyutada va kurs.")
        st.markdown("**Misol:** `1000 USD` → Markaziy bank kursi bo'yicha so‘zlanadi.")
        st.markdown("**Qoidalar:** Agar bitim shartlari o'zaro bog'liq tomonlarga taalluqli bo'lsa, 1-usul qo'llanmasligi mumkin. :contentReference[oaicite:9]{index=9}")

    with st.expander("4. Grafa — Bilvosita to'lovlar (11b va 12 grafa)", expanded=False):
        st.markdown("**Maqsad:** Tovar qiymatiga qo'shilishi kerak bo'lgan uchinchi shaxslarga to'lovlar (misol: litsenziya, komissiya).")
        st.markdown("**Nima kiritiladi:** Toʻlov summalari va asos (kontrakt bo'yicha yoki qo'shimcha hujjatlar).")
        st.markdown("**Misol:** `Litsenziya to'lovi: 50 USD`")

    with st.expander("5. Grafa — Soliqlar va bojxona to'lovlari asoslari", expanded=False):
        st.markdown("**Maqsad:** Bojxona qiymatini ta'sir qiluvchi mahalliy soliqlar (ba'zi hollarda chegirish/kiritish talab qilinadi).")
        st.markdown("**Nima kiritiladi:** To‘lanishi yoki chetlatilishi kerak bo‘lgan soliqlar ro'yxati va summasi.")

    with st.expander("6. Grafa — Qo'shimcha xarajatlar (transport, sug'urta, yuklash)", expanded=False):
        st.markdown("**Maqsad:** Bitim narxiga kiritilmagan, ammo bojxona qiymatiga qo‘shilishi kerak bo‘lgan xarajatlar.")
        st.markdown("**Nima kiritiladi:** Tashish, sug'urta, yuklash/tushirish summalari va hujjat manbalari.")
        st.markdown("**Eslatma:** Har bir element uchun hujjat (invoys, bill of lading, insurance policy) talab qilinadi.")

    with st.expander("7. Grafa — Bog'liqlik (7a/7b)", expanded=False):
        st.markdown("**Maqsad:** Sotuvchi va xaridor orasidagi bog'liqlik (affiliated parties) aniqlash.")
        st.markdown("**Ta'siri:** Agar bog'liqlik aniqlansa va narxga ta'sir qilgan bo'lsa — 1-usul qo'llanilmaydi va boshqa usullarga o'tiladi. :contentReference[oaicite:10]{index=10}")

    with st.expander("8. Grafa — Cheklovlar va shartnomalar", expanded=False):
        st.markdown("**Maqsad:** Narxga cheklovlar (masalan, qaytarish shartlari), tovarni shartli sotish holatlari.")
        st.markdown("**Ta'siri:** Shunday shartlar mavjud bo'lsa, 1-usul qoidalaridan voz kechish zarur.")

    # Continue for other grafalar up to 23 with concise explanations:
    grafalar = {
        9: ("Intellektual mulk to'lovlari (9a)", "Litsenziya, mualliflik haqi, patent va shu kabilar."),
        10: ("Qayta sotishdan tushum (9b)", "Keyingi sotishdan olinadigan ulush va shartnoma bo'yicha tushumlar."),
        11: ("Hisoblash formulalari", "BOJXONA QIYMATI = (12 + 18) - 22 kabi yakuniy formula."),
        12: ("Qo'shimcha varaq va izohlar", "Hujjatlar ro'yxati va BYD raqami misollari."),
        13: ("Tuzatishlar bo'limi (B bo'lim)", "Vositachilik haqlari, konteyner, o'rov, ishlab chiqarish xarajatlari."),
        14: ("Yetkazib berish shartlari tafsiloti", "INCOTERMS farqlashlari va ularning hisoblashdagi ta'siri."),
        15: ("Hisob-kitob misollari", "Amaliy misollar (1-usulga oid oddiy hisoblardan murakkab holatlarga qadar)."),
        16: ("2-usul uchun maxsus grafalar", "Aynan bir xil tovar BYD raqamlari va 90 kun qoidasi."),
        17: ("3-usul uchun xususiy talablar", "O'xshash tovarlar, xususiyat va sifat mosligi."),
        18: ("4-usul — chegirish usuli tafsiloti", "Ichki bozordagi narxni chegirib hisoblash qoidalari. :contentReference[oaicite:11]{index=11}"),
        19: ("5-usul — qo'shish (hisoblangan qiymat)", "Ishlab chiqarish xarajatlari, umumiy xarajatlar va odatiy foyda."),
        20: ("6-usul — zaxira", "Yuqoridagi usullar yetarli bo'lmaganda tatbiq etiladi."),
        21: ("Qayerga ilova qilish kerak", "Hujjatlarni qanday tartibda yig'ish va elektron tizimda joylashtirish."),
        22: ("Imzo, sana, va tasdiq", "ERI va muhr talablari; BYD bilan bir vaqtda topshirish majburiyati. :contentReference[oaicite:12]{index=12}"),
        23: ("Yakuni — Bojxona qiymati (23a)", "Hisoblangan bojxona qiymati va unga asoslangan to'lovlar.")
    }

    for k, v in grafalar.items():
        title, desc = v
        with st.expander(f"{k}. {title}", expanded=False):
            st.markdown(f"**Izoh:** {desc}")
            # Add an example area for each grafa
            st.markdown("**Misol:**")
            if k in (11, 23):
                st.markdown("<div class='formula'>BOJXONA QIYMATI = (12 + 18) - 22</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='example'>Tegishli ma'lumotni shu yerga yozing (grafa {k})</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")
    nav_buttons()

elif selected == "💡 Muhim qoidalar va misollar":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='info-title'>Eng muhim amaliy qoidalar</div>", unsafe_allow_html=True)
    st.markdown("""
- **1-usulni faqat shartlar bajarilganda qo'llang** — agar sotuvchi va xaridor o'rtasida bog'liqlik, narx cheklovlari yoki boshqa ta'sir etuvchi omillar mavjud bo'lsa, 1-usul ishlatilmaydi. :contentReference[oaicite:13]{index=13}  
- **90 kun qoidasi (2/3-usullar uchun)** — aynan bir xil yoki o'xshash tovar bo'yicha ma'lumotlar so'nggi 90 kun ichida olinishi kerak. :contentReference[oaicite:14]{index=14}  
- **Hujjatlar asosiy dalil** — sug'urta polisisi, tashish hujjatlari, invoys va TEDAAT kontraktlari bojxona qiymatini tasdiqlashda muhim rol o'ynaydi. :contentReference[oaicite:15]{index=15}
""")
    st.markdown("### Amaliy misol: FOB kontrakt → Bojxona qiymatini qanday hisoblash")
    st.markdown("1) Kontrakt narxini (FOB) oling. 2) FOB ga navlun va sug'urta qo'shing (agar kontrakt narxiga kiritilmagan bo'lsa). 3) Valyuta kursiga ko'ra milliy valyutaga o'tkazing. 4) Tuzatishlar (komissiya, litsenziya) qo'shing. 5) Yakuniy summa 23-grafa.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")
    nav_buttons()

elif selected == "📎 Hujjatlar va isbotlovchi ma'lumotlar":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='info-title'>Asosiy hujjatlar ro'yxati</div>", unsafe_allow_html=True)
    st.markdown("""
**1-usul uchun majburiy:**
- Tashqi savdo kontrakti (TEDAAT ID), invoys, tashish hujjatlari (B/L yoki CMR), sug'urta polisisi, bank to'lov hujjatlari. :contentReference[oaicite:16]{index=16}

**2/3-usullar uchun qo'shimcha:**
- Oldingi BYD raqamlari (90 kun ichida), taqqoslovchi invoyslar, transport xarajatlarini tasdiqlovchi hujjatlar. :contentReference[oaicite:17]{index=17}

**4/5-usullar uchun:**
- O'zbekiston ichidagi sotuv hujjatlari (4-usul), ishlab chiqaruvchining buxgalteriya hisoboti va ishlab chiqarish kalkulyatsiyalari (5-usul). :contentReference[oaicite:18]{index=18}
""")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")
    nav_buttons()

elif selected == "⚠️ Xatoliklar va tavsiyalar":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='info-title'>Tez-tez uchraydigan xatolar</div>", unsafe_allow_html=True)
    st.error("""
- 1-usulni noto'g'ri qo'llash (bog'liqlik e'tiborga olinmagan).  
- Tuzatishlar (transport, sug'urta) unutilgan.  
- Valyuta kursi noto'g'ri qo'llanilgan.  
- Hujjatlar to'liq emas yoki mos kelmaydi.  
- Grafalarni noto'g'ri to'ldirish yoki BYD bilan mos kelmaslik.
""")
    st.markdown("### Tavsiya:")
    st.markdown("""
1. Hujjatlarni oldindan to'plang.  
2. Har bir grafa uchun manbani (hujjat) yozib qo'ying.  
3. Elektron raqamli imzo (ERI) bilan tasdiqlashni tekshiring.  
4. Shubhali holatda bojxona organi yoki vakolatli brokerga murojaat qiling.
""")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")
    nav_buttons()

elif selected == "✅ Xulosa":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='info-title'>Xulosa va Qo'llanma</div>", unsafe_allow_html=True)
    st.markdown("""
- BQD — bojxona rasmiylashtiruvi uchun hal qiluvchi hujjat; har bir grafa to'liq va aniq to'ldirilishi lozim. :contentReference[oaicite:19]{index=19}  
- Asosiy manbalar: Yo'riqnoma, Bojxona kodeksi va Vazirlar Mahkamasi qarorlari. :contentReference[oaicite:20]{index=20}
""")
    st.markdown("<div class='small-muted'>So'nggi yangilanish: avvalgi rasmiy yo'riqnomalar va qarorlarni tekshiring. (lex.uz saytida rasmiy matnlar mavjud.)</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    nav_buttons()

# FOOTER
st.markdown(
    f"""
    <div class='footer'>
        <div><strong>BQD Interaktiv — {datetime.now().year}</strong></div>
        <div class='small-muted'>Rasmiy hujjatlar va yo'riqnomalarni lex.uz saytidan tekshiring. (Yo'riqnoma / qarorlar havolalari sidebarda keltirilgan.)</div>
    </div>
    """,
    unsafe_allow_html=True,
)




