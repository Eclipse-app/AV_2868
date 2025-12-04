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




















import streamlit as st

# ==================== SAHIFA SOZLAMALARI ====================
st.set_page_config(
    page_title="BQD — Bojxona Qiymat Deklaratsiyasi",
    page_icon="🇺🇿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== ZAMONAVIY CSS ====================
st.markdown("""
<style>
    .main-title {
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #1e40af, #7c3aed);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.4rem;
        color: #64748b;
        text-align: center;
        margin-bottom: 3rem;
    }
    .card {
        padding: 1.8rem;
        border-radius: 16px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        border-left: 6px solid;
    }
    .card-blue   { background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); border-left-color: #3b82f6; }
    .card-green  { background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border-left-color: #22c55e; }
    .card-purple { background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%); border-left-color: #a855f7; }
    .card-orange { background: linear-gradient(135deg, #fff7ed 0%, #fed7aa 100%); border-left-color: #f97316; }
    .card-red    { background: linear-gradient(135deg, #fef2f2 0%, #fecaca 100%); border-left-color: #ef4444; }
    .card-yellow { background: linear-gradient(135deg, #fefce8 0%, #fef9c3 100%); border-left-color: #eab308; }
    .section-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1e293b;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e2e8f0;
    }
    .formula-box {
        background: #1e293b;
        color: #60a5fa;
        padding: 1.5rem;
        border-radius: 12px;
        font-family: 'Courier New', monospace;
        font-size: 1.3rem;
        text-align: center;
        font-weight: bold;
        margin: 2rem 0;
    }
    .footer {
        text-align: center;
        padding: 3rem 1rem;
        background: #0f172a;
        color: #e2e8f0;
        margin-top: 4rem;
        border-radius: 16px;
    }
</style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR NAVIGATSIYA ====================
st.sidebar.title("🇺🇿 BQD Taqdimoti")
st.sidebar.markdown("**Bojxona Qiymat Deklaratsiyasi**")
st.sidebar.markdown("---")

slides = [
    "Kirish",
    "BQD Turlari",
    "Taqdim Shakllari",
    "BQD-1 (1-usul) – Batafsil",
    "BQD-1 Muhim Grafalar",
    "BQD-2 (2-6 usullar)",
    "Kerakli Hujjatlar",
    "Muhim Eslatmalar",
    "Video Qo‘llanma",
    "Xulosa"
]

icons = ["🏠", "📊", "💻", "📝", "⚠️", "📋", "📎", "⚡", "🎥", "✅"]
slide_dict = {f"{icon} {name}": name for icon, name in zip(icons, slides)}

current_slide = st.sidebar.radio("Bo‘limni tanlang:", list(slide_dict.keys()))

# ==================== ASOSIY KONTENT ====================
title = slide_dict[current_slide]

if title == "Kirish":
    st.markdown('<h1 class="main-title">Bojxona Qiymat Deklaratsiyasi (BQD)</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">O‘zbekiston Respublikasi bojxona hududiga olib kiriladigan tovarlar uchun majburiy hujjat</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Uzbekistan.png", width=150)
    
    st.markdown("""
    <div class="card card-blue">
        <h3>📖 BQD nima?</h3>
        <p><strong>Bojxona Qiymat Deklaratsiyasi (BQD)</strong> — Bojxona yuk deklaratsiyasining (BYD) ajralmas qismi bo‘lib, 
        tovarning bojxona qiymati to‘g‘risidagi to‘liq ma’lumotlarni o‘z ichiga oladi. Deklarant yoki bojxona brokeri tomonidan 
        BYD bilan bir vaqtda bojxona organiga taqdim etiladi.</p>
        <p><strong>Qonuniy asos:</strong> O‘zbekiston Respublikasi Bojxona kodeksining <strong>303–313-moddalari</strong></p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card card-green"><h4>📄 BQD-1</h4><p>1-usul (bitim qiymati) uchun<br><strong>90%+ hollarda qo‘llaniladi</strong></p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card card-purple"><h4>📋 BQD-2</h4><p>2–6 usullar uchun<br>1-usul qo‘llab bo‘lmaganda</p></div>', unsafe_allow_html=True)

elif title == "BQD Turlari":
    st.markdown('<h1 class="main-title">BQD Turlari va Qo‘llanilishi</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card card-green">
        <h3>1-usul – Bitim qiymati (BQD-1)</h3>
        <ul>
            <li>Eng keng tarqalgan usul (90%+)</li>
            <li>Sotuvchi va xaridor o‘rtasida haqiqiy savdo bitimi mavjud</li>
            <li>Narx hujjatlar bilan tasdiqlangan</li>
            <li>Hech qanday cheklov va o‘zaro bog‘liqlik ta’sir qilmagan</li>
        </ul>
    </div>
    
    <div class="card card-purple">
        <h3>2–6 usullar (BQD-2)</h3>
        <p>1-usul qo‘llab bo‘lmaganda ketma-ketlikda qo‘llaniladi:</p>
        <div style="columns: 2;">
            <li>2-usul → Aynan bir xil tovar</li>
            <li>3-usul → O‘xshash tovar</li>
            <li>4-usul → Chegirish usuli</li>
            <li>5-usul → Qo‘shish usuli</li>
            <li>6-usul → Zaxira usul</li>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif title == "Taqdim Shakllari":
    st.markdown('<h1 class="main-title">Taqdim Etish Shakllari</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card card-blue">
            <h3>📱 Elektron shakl (afzal)</h3>
            <ul>
                <li>TEDAAT orqali</li>
                <li>ERI (elektron raqamli imzo) bilan</li>
                <li>Tez, xatosiz, arxivlanadi</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card card-orange">
            <h3>📄 Qog‘oz shakl</h3>
            <ul>
                <li>A4 formatda 4 nusxa</li>
                <li>Imzo + muhr</li>
                <li>Elektron nusxa ham ERI bilan</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif title == "BQD-1 (1-usul) – Batafsil":
    st.markdown('<h1 class="main-title">BQD-1 To‘ldirish – Batafsil Tushuntirish</h1>', unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Har bir grafa rasmiy talablar asosida tushuntirilgan</p>", unsafe_allow_html=True)

    with st.expander("A BO‘LIM – Hisoblash uchun asos (11–12-grafalar)", expanded=True):
        st.markdown("""
        <div class="card card-blue">
            <strong>11a-grafa</strong> → Bitim narxi (invoys bo‘yicha)<br>
            &nbsp;&nbsp;• 1-qator: kontrakt valyutasida<br>
            &nbsp;&nbsp;• 2-qator: so‘mda (Markaziy bank kursi bo‘yicha)<br>
            &nbsp;&nbsp;• 3-qator: qo‘llanilgan kurs<br><br>
            <strong>11b-grafa</strong> → Bilvosita to‘lovlar (royalti, litsenziya, vositachilik va h.k.)<br><br>
            <strong>12-grafa</strong> → Jami A bo‘lim = 11a + 11b
        </div>
        """, unsafe_allow_html=True)

    with st.expander("B BO‘LIM – Qo‘shimcha hisoblar (+)", expanded=True):
        st.markdown("""
        <div class="card card-green">
            <strong>13–17 grafalar</strong> → Bojxona qiymatiga qo‘shiladigan xarajatlar:<br>
            • 13a – vositachilik haqi<br>
            • 14 – konteyner va o‘rov<br>
            • 15 – mualliflik, litsenziya to‘lovlari<br>
            • 16 – qayta sotishdan sotuvchiga tushadigan daromad<br>
            • 17a – tashish, 17b – yuklash/tushirish, 17v – sug‘urta<br><br>
            <strong>18-grafa</strong> → B bo‘lim yig‘indisi
        </div>
        """, unsafe_allow_html=True)

    with st.expander("V BO‘LIM – Chegirmalar (–)", expanded=True):
        st.markdown("""
        <div class="card card-red">
            <strong>19–22 grafalar</strong> → O‘zbekistonda yuzaga kelgan xarajatlar:<br>
            • 19 – qurilish, montaj<br>
            • 20 – O‘zbekiston ichidagi transport<br>
            • 21 – bojxona to‘lovlari va soliqlar<br>
            • 22 – V bo‘lim yig‘indisi
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="formula-box">
        BOJXONA QIYMATI = (12-grafa + 18-grafa) − 22-grafa<br>
        → Bu qiymat 23a-grafada ko‘rsatiladi
    </div>
    """, unsafe_allow_html=True)

elif title == "BQD-1 Muhim Grafalar":
    st.markdown('<h1 class="main-title">Eng Muhim va "Xavfli" Grafalar</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card card-red">
            <h4>7a-7b grafalar – O‘zaro bog‘liqlik</h4>
            <p>Agar "HA" bo‘lsa va bog‘liqlik narxga ta’sir qilgan bo‘lsa → <strong>1-usul qo‘llanilmaydi!</strong></p>
        </div>
        <div class="card card-yellow">
            <h4>8a-8b grafalar – Cheklovlar</h4>
            <p>Narxga ta’sir etuvchi cheklovlar bo‘lsa → 1-usul yo‘q!</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card card-purple">
            <h4>9a-grafa – Intellektual mulk to‘lovlari</h4>
            <p>Litsenziya, royalti, patent, savdo belgisi uchun to‘lovlar → majburiy qo‘shiladi</p>
        </div>
        <div class="card card-orange">
            <h4>3-grafa – Yetkazib berish shartlari (INCOTERMS)</h4>
            <p>EXW, FCA, FOB, CIF, CIP va boshqalar → to‘g‘ri ko‘rsatilmasa katta xato!</p>
        </div>
        """, unsafe_allow_html=True)

elif title == "BQD-2 (2-6 usullar)":
    st.markdown('<h1 class="main-title">BQD-2 – 2-6 usullar batafsil</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["2-usul", "3-usul", "4-usul", "5-usul", "6-usul"])
    
    with tab1:
        st.markdown("""
        <div class="card card-blue">
            <h3>2-usul: Aynan bir xil tovar bitimi</h3>
            <p>So‘nggi 90 kun ichida olib kirilgan, bojxona tomonidan qabul qilingan, aynan bir xil tovarning narxi asos qilib olinadi.</p>
            <p><strong>Muhim:</strong> miqdor, tijorat shartlari, transport xarajatlari bo‘yicha tuzatishlar kiritiladi.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class="card card-green">
            <h3>3-usul: O‘xshash tovar bitimi</h3>
            <p>2-usul bilan deyarli bir xil, faqat “aynan bir xil” o‘rniga “o‘xshash” tovar ishlatiladi.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class="card card-orange">
            <h3>4-usul: Chegirish usuli</h3>
            <p>O‘zbekistonda sotilgan narxdan vositachilik, soliq, ichki transport xarajatlari chegirib tashlanadi.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("""
        <div class="card card-red">
            <h3>5-usul: Qo‘shish usuli (hisoblangan qiymat)</h3>
            <p>Ishlab chiqaruvchi xarajatlari + odatdagi foyda + transport = bojxona qiymati</p>
            <p><strong>Talab:</strong> ishlab chiqaruvchining buxgalteriya hujjatlari</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab5:
        st.markdown("""
        <div class="card card-purple">
            <h3>6-usul: Zaxira usul</h3>
            <p>Yuqoridagi 5 usulning hech biri qo‘llanmasa → bojxona xodimi professional mulohaza yuritadi (lekin 1-5 usullarga zid bo‘lmasligi kerak).</p>
        </div>
        """, unsafe_allow_html=True)

elif title == "Kerakli Hujjatlar":
    st.markdown('<h1 class="main-title">Taqdim etilishi kerak bo‘lgan hujjatlar</h1>', unsafe_allow_html=True)
    
    tabs = st.tabs(["1-usul", "2-3 usullar", "4-usul", "5-usul"])
    with tabs[0]:
        st.markdown("""
        <div class="card card-blue">
            <h4>Majburiy:</h4>
            <li>Tashqi savdo kontrakti (TEDAAT ID)</li>
            <li>Invoys (hisob-faktura)</li>
            <h4>Qo'shimcha (zarur bo‘lganda):</h4>
            <li>Sug‘urta polisi</li>
            <li>Transport shartnomasi va hujjatlar</li>
            <li>Litsenzion kelishuv</li>
            <li>Bank to‘lov hujjatlari</li>
        </div>
        """, unsafe_allow_html=True)

elif title == "Muhim Eslatmalar":
    st.markdown('<h1 class="main-title">Eng muhim eslatmalar</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card card-red">
        <h4>Qat'iy talablar</h4>
        <li>O‘chirish, bo‘yash bo‘lmasligi kerak</li>
        <li>Barcha summalar milliy valyutada</li>
        <li>ERI bilan tasdiqlanishi shart</li>
        <li>Hujjatlar rus yoki ingliz tilida (boshqa tillarda – tarjima bilan)</li>
    </div>
    
    <div class="card card-yellow">
        <h4>Muddatlar</h4>
        <li>2-4 usullar uchun → 90 kun</li>
        <li>Muqobil manbalar → 180 kun</li>
        <li>BYD bilan bir vaqtda taqdim etiladi</li>
    </div>
    """, unsafe_allow_html=True)

elif title == "Video Qo‘llanma":
    st.markdown('<h1 class="main-title">Video qo‘llanma</h1>', unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=ke5_OKgJs_E")
    st.markdown("""
    <div class="card card-blue" style="text-align:center; padding:2rem;">
        <h4>BQD-1 va BQD-2 ni to‘ldirish bo‘yicha batafsil video darslik</h4>
        <p>Muallif: Bojxona xizmati xodimi, 2024-yil</p>
    </div>
    """, unsafe_allow_html=True)

elif title == "Xulosa":
    st.markdown('<h1 class="main-title">Xulosa va tavsiyalar</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card card-green">
        <h3>Asosiy qoidalar</h3>
        <li>Aniqlik – To‘liqlik – Hujjatlilik – Vaqtida taqdim etish</li>
        <li>1-usul → 90%+ hollarda</li>
        <li>Bog‘liqlik va cheklovlarni unutmaslik!</li>
    </div>
    
    <div style="text-align:center; margin-top:3rem;">
        <h2 style="color:#22c55e;">E’tiboringiz uchun katta rahmat!</h2>
        <p>Savollar bo‘lsa – bojxona brokeri yoki yaqin bojxona bo‘limiga murojaat qiling</p>
    </div>
    """, unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown("""
<div class="footer">
    <h3>Bojxona Qiymat Deklaratsiyasi (BQD) taqdimoti</h3>
    <p>O‘zbekiston Respublikasi Bojxona kodeksi (303–313-moddalar) • 2025-yil yangilanishi</p>
    <p><strong>Manba:</strong> <a href="https://lex.uz/docs/-3133231" style="color:#60a5fa;">lex.uz – O‘zbekiston Respublikasi qonunchiligi</a> | 
    <a href="https://customs.uz" style="color:#60a5fa;">customs.uz</a></p>
    <p style="font-size:0.9rem; margin-top:1rem;">So‘nggi yangilanish: 2025-yil dekabr</p>
</div>
""", unsafe_allow_html=True)

# ==================== NAVIGATSIYA TUGMALARI ====================
st.markdown("---")
col_prev, col_info, col_next = st.columns([1, 2, 1])
current_idx = slides.index(title)

with col_prev:
    if current_idx > 0:
        if st.button("⬅️ Oldingi bo‘lim", use_container_width=True):
            st.session_state.current = slides[current_idx - 1]
            st.rerun()

with col_info:
    st.markdown(f"<p style='text-align:center; font-size:1.2rem; color:#64748b;'><strong>{current_idx + 1}</strong> / {len(slides)}</p>", unsafe_allow_html=True)

with col_next:
    if current_idx < len(slides) - 1:
        if st.button("Keyingi bo‘lim ➡️", use_container_width=True):
            st.session_state.current = slides[current_idx + 1]
            st.rerun()

# Sidebar qo‘shimcha maslahatlar
with st.sidebar:
    st.markdown("---")
    st.markdown("### Maslahatlar")
    st.info("Hujjatlarni oldindan tayyorlang")
    st.success("Grafalarni ketma-ket to‘ldiring")
    st.warning("Valyuta kursini unutmeng")
    st.error("Bog‘liqlik va cheklovlarni tekshiring")