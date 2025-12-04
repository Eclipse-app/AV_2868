import streamlit as st

# Sahifa sozlamalari
st.set_page_config(
    page_title="BQD Taqdimoti",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS stillari
st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1e40af;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #64748b;
        text-align: center;
        margin-bottom: 2rem;
    }
    .info-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .blue-box {
        background-color: #eff6ff;
        border-left: 4px solid #3b82f6;
    }
    .green-box {
        background-color: #f0fdf4;
        border-left: 4px solid #22c55e;
    }
    .purple-box {
        background-color: #faf5ff;
        border-left: 4px solid #a855f7;
    }
    .orange-box {
        background-color: #fff7ed;
        border-left: 4px solid #f97316;
    }
    .red-box {
        background-color: #fef2f2;
        border-left: 4px solid #ef4444;
    }
    .yellow-box {
        background-color: #fefce8;
        border-left: 4px solid #eab308;
    }
    .section-title {
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .formula {
        font-family: monospace;
        font-size: 1.1rem;
        text-align: center;
        padding: 1rem;
        background-color: #f8fafc;
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigatsiya
st.sidebar.title("📑 Taqdimot Bo'limlari")
st.sidebar.markdown("---")

slides = [
    "🏠 Kirish",
    "📊 BQD Turlari",
    "💻 Taqdim Shakllari",
    "📝 BQD-1 To'ldirish",
    "⚠️ Muhim Grafalari",
    "📋 BQD-2 To'ldirish",
    "📎 Hujjatlar",
    "⚡ Eslatmalar",
    "✅ Xulosa"
]

current_slide = st.sidebar.radio("Bo'limni tanlang:", slides, index=0)

# Asosiy kontent
if current_slide == "🏠 Kirish":
    st.markdown('<p class="main-title">📋 Bojxona Qiymat Deklaratsiyasi (BQD)</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">O\'zbekiston Respublikasi bojxona hududiga olib kiriladigan tovarlar uchun</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box blue-box">', unsafe_allow_html=True)
    st.markdown("### 📖 Asosiy Ta'rif")
    st.write("""
    **BQD** — bojxona yuk deklaratsiyasining (BYD) ajralmas qismi bo'lib, 
    tovarning bojxona qiymati to'g'risidagi ma'lumotlar ko'rsatilgan va 
    deklarant yoki bojxona brokeri tomonidan bojxona organiga BYD bilan 
    bir paytda topshiriladigan hujjat.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
        st.markdown("#### 📄 BQD-1")
        st.write("1-usul (bitim qiymati) uchun")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="info-box purple-box">', unsafe_allow_html=True)
        st.markdown("#### 📋 BQD-2")
        st.write("2-6 usullar uchun")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.info("ℹ️ BQD Bojxona kodeksining 303-313-moddalariga muvofiq to'ldiriladi")

elif current_slide == "📊 BQD Turlari":
    st.markdown('<p class="main-title">📊 BQD Turlari va Qo\'llanilishi</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
    st.markdown("### ✅ BQD-1 (1-usul)")
    st.write("**Olib kiriladigan tovarga doir bitimning qiymatiga oid usul**")
    st.markdown("""
    - ✓ Sotuvchi va sotib oluvchi o'rtasida to'g'ridan-to'g'ri sotish-sotib olish bitimi mavjud
    - ✓ Bitim narxi aniq va hujjat bilan tasdiqlangan
    - ✓ Eng keng qo'llaniladigan usul
    - ✓ 90% dan ortiq holatlarda ishlatiladi
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box purple-box">', unsafe_allow_html=True)
    st.markdown("### 🔄 BQD-2 (2-6 usullar)")
    st.write("**1-usulni qo'llab bo'lmaganda qo'llaniladigan alternativ usullar**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **2-usul:** Aynan bir xil tovar bitimi  
        **3-usul:** O'xshash tovar bitimi  
        **4-usul:** Qiymatlarni chegirish usuli
        """)
    with col2:
        st.markdown("""
        **5-usul:** Qiymatlarni qo'shish usuli  
        **6-usul:** Zaxira usul (1-5 asosida)
        """)
    st.markdown('</div>', unsafe_allow_html=True)

elif current_slide == "💻 Taqdim Shakllari":
    st.markdown('<p class="main-title">💻 BQD Taqdim Etish Shakllari</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="info-box blue-box">', unsafe_allow_html=True)
        st.markdown("### 📱 Elektron shakl")
        st.markdown("""
        ✅ TEDAAT tizimi orqali  
        ✅ Elektron raqamli imzo (ERI) bilan  
        ✅ BYD elektron bo'lsa, BQD ham elektron  
        ✅ Tezkor va qulay
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="info-box orange-box">', unsafe_allow_html=True)
        st.markdown("### 📄 Qog'oz shakl")
        st.markdown("""
        ✅ A4 formatda 4 nusxada  
        ✅ Elektron nusxasi ERI bilan  
        ✅ Imzo va muhur zarur
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
    st.markdown("### 📑 Nusxalar Taqsimoti (Qog'oz shakl)")
    st.markdown("""
    1. **1-nusxa:** Bojxona organlari uchun (arxivda saqlanadi)
    2. **2-nusxa:** Deklaratsiyalovchi shaxs uchun
    3. **3-4 nusxalar:** Deklarant uchun
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif current_slide == "📝 BQD-1 To'ldirish":
    st.markdown('<p class="main-title">📝 BQD-1 To\'ldirish Tartibi</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Asosiy grafalar va ularning mazmuni</p>', unsafe_allow_html=True)
    
    with st.expander("🔵 A BO'LIM: Hisoblash uchun asos", expanded=True):
        st.markdown("""
        **11a-grafa:** Bitim narxi
        - 1-qator: Kontrakt valyutasida
        - 2-qator: Milliy valyutada
        - 3-qator: Valyuta kursi
        
        **11b-grafa:** Bilvosita to'lovlar summasi
        - Sotuvchi manfaati uchun uchinchi shaxslarga to'lovlar
        - Bitim narxiga tuzatishlar
        
        **12-grafa:** Jami = 11a + 11b
        """)
    
    with st.expander("🟢 B BO'LIM: Qo'shimcha hisoblar"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **13a:** Vositachilik haqlari  
            **13b:** Konteyner va o'rov-joylov  
            **14:** Xomashyo, materiallar  
            **15:** Litsenziya to'lovlari
            """)
        with col2:
            st.markdown("""
            **16:** Qayta sotishdan tushum  
            **17a:** Tashish xarajatlari  
            **17b:** Yuklash/tushirish  
            **17v:** Sug'urta
            """)
        st.markdown("**18-grafa:** B bo'lim yig'indisi")
    
    with st.expander("🔴 V BO'LIM: Chegirmalar"):
        st.markdown("""
        **19-grafa:** Qurilish, montaj xarajatlari (O'zbekistonda)  
        **20-grafa:** O'zbekiston ichida tashish  
        **21-grafa:** Bojxona va boshqa to'lovlar  
        **22-grafa:** V bo'lim yig'indisi
        """)
    
    st.markdown('<div class="info-box purple-box">', unsafe_allow_html=True)
    st.markdown("### 🧮 Yakuniy Hisob-kitob")
    st.markdown('<p class="formula"><strong>BOJXONA QIYMATI = (12 + 18) - 22</strong></p>', unsafe_allow_html=True)
    st.markdown("Bu qiymat **23a-grafa**da ko'rsatiladi va bojxona to'lovlarini hisoblash uchun asos bo'ladi.")
    st.markdown('</div>', unsafe_allow_html=True)

elif current_slide == "⚠️ Muhim Grafalari":
    st.markdown('<p class="main-title">⚠️ BQD-1: Muhim va Tanqidiy Grafalari</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box yellow-box">', unsafe_allow_html=True)
    st.markdown("### ❓ 7a-7b grafalar: O'zaro bog'liqlik")
    st.write("**Savol:** Sotuvchi va sotib oluvchi o'rtasida o'zaro bog'liqlik mavjudmi?")
    st.warning("""
    ⚠️ Agar "Ha" javob berilsa va bog'liqlik bitim narxiga ta'sir qilgan bo'lsa:
    - 1-usul qo'llanilmaydi
    - BQD-2 to'ldirilishi kerak
    - 2-6 usullardan biri tanlanadi
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box red-box">', unsafe_allow_html=True)
    st.markdown("### 🚫 8a-8b grafalar: Shartlar va cheklovlar")
    st.write("**Savol:** Sotish yoki bitimning bahosiga cheklovlar bormi?")
    st.error("""
    🛑 Quyidagi hollarda 1-usul qo'llanilmaydi:
    - Shartlarni miqdoriy baholash mumkin emas
    - Tovarni qaytarish talablari mavjud
    - Narxga ta'sir etuvchi aniqlanmagan omillar bor
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="info-box blue-box">', unsafe_allow_html=True)
        st.markdown("### 💡 9a-grafa")
        st.write("**Intellektual mulk to'lovlari**")
        st.markdown("""
        - Litsenziya to'lovlari
        - Mualliflik haqi
        - Patent to'lovlari
        - Tovar belgisi uchun
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
        st.markdown("### 💰 9b-grafa")
        st.write("**Qayta sotishdan tushum**")
        st.markdown("""
        - Sotuvchiga tegishli ulush
        - Daromadning foizi
        - Keyingi sotishdan foyda
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
    st.markdown("### 🚚 3-grafa: Yetkazib berish shartlari (INCOTERMS)")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**EXW** - Zavod narxi")
        st.info("**FCA** - Tashuvchiga topshirish")
    with col2:
        st.success("**FOB** - Bortda erkin")
        st.success("**CFR** - Narx + navlun")
    with col3:
        st.warning("**CIF** - Narx + sug'urta + navlun")
        st.warning("**CIP** - Navlun to'langan")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif current_slide == "📋 BQD-2 To'ldirish":
    st.markdown('<p class="main-title">📋 BQD-2 To\'ldirish Tartibi</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">2-6 usullar uchun maxsus shakl</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box purple-box">', unsafe_allow_html=True)
    st.markdown("### 📄 Asosiy Varaq (Barcha usullar uchun)")
    st.markdown("""
    **6-grafa:** Qo'llaniladigan usulga "X" belgisi  
    **7-grafa:** Oldingi usullarni qo'llab bo'lmaslik sabablari (majburiy)  
    **8-grafa:** Taqdim etilgan asosiy hujjatlar ro'yxati  
    **9-grafa:** Qo'shimcha varaqlar soni  
    **10-grafa:** Joy, sana va imzo
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["2-usul", "3-usul", "4-usul", "5-usul"])
    
    with tab1:
        st.markdown('<div class="info-box blue-box">', unsafe_allow_html=True)
        st.markdown("### 🔵 2-usul: Aynan bir xil tovar")
        st.markdown("""
        **11-grafa:** Aynan bir xil tovarga doir bitim qiymati
        - So'nggi 90 kun ichida olib kirilgan
        - Bojxona organi tomonidan qabul qilingan
        - 1-usul bo'yicha aniqlangan
        
        **B bo'lim (12a-15):** Tuzatishlar
        - Miqdor farqi (12a, 14a)
        - Tijorat shartlari (12b, 14b)
        - Tashish xarajatlari (12v, 14v)
        - Yuklash/tushirish (12g, 14g)
        - Sug'urta (12d, 14d)
        
        **16-grafa:** Tuzatilgan bitim qiymati  
        **18a-grafa:** Bojxona qiymati = (16 × 17b) ÷ 17a  
        **20-grafa:** Ma'lumot manbai (BYD raqami)
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
        st.markdown("### 🟢 3-usul: O'xshash tovar")
        st.write("**2-usul bilan bir xil tartibda, lekin:**")
        st.markdown("""
        - Aynan bir xil o'rniga o'xshash tovar ishlatiladi
        - Tovar xususiyatlari, sifati va obro'si o'xshash bo'lishi kerak
        - Bir xil mamlakat ishlab chiqaruvchisidan
        - Grafalarni to'ldirish 2-usul kabi
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="info-box orange-box">', unsafe_allow_html=True)
        st.markdown("### 🟠 4-usul: Qiymatlarni chegirish")
        st.markdown("""
        **11-grafa:** O'zbekistonda sotilgan tovar birligi narxi
        - So'nggi 90 kun ichida sotilgan
        - Dastlabki holatda (ishlov berilmagan)
        
        **B bo'lim (12-16):** Chegirib tashlanadi:
        - **12:** Vositachilik haqi va umumiy xarajatlar
        - **13:** Bojxona to'lovlari va soliqlar
        - **14:** Transport xarajatlari O'zbekistonda
        - **15:** Ishlov berish qiymati (agar mavjud)
        
        **18a-grafa:** (11 - 16) × 17 = Bojxona qiymati
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab4:
        st.markdown('<div class="info-box red-box">', unsafe_allow_html=True)
        st.markdown("### 🔴 5-usul: Qiymatlarni qo'shish (Hisoblangan qiymat)")
        st.markdown("""
        **11-grafa:** Ishlab chiqarish xarajatlari
        - Xomashyo va materiallar
        - Ishlab chiqarish jarayoni
        - O'rash-joylash
        
        **12-grafa:** Umumiy xarajatlar + foyda
        - Ishlab chiqaruvchi umumiy xarajatlari
        - Oddiy darajadagi foyda
        
        **13-15:** Transport xarajatlari
        - Tashish (13)
        - Yuklash/tushirish (14)
        - Sug'urta (15)
        
        **16a-grafa:** 11 + 12 + 13 + 14 + 15 = Bojxona qiymati
        """)
        st.info("⚠️ Ishlab chiqaruvchining buxgalterlik hisoblari asosida!")
        st.markdown('</div>', unsafe_allow_html=True)

elif current_slide == "📎 Hujjatlar":
    st.markdown('<p class="main-title">📎 Taqdim Etilishi Kerak Hujjatlar</p>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["1-usul", "2-3 usullar", "4-usul", "5-usul"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="info-box blue-box">', unsafe_allow_html=True)
            st.markdown("### ✅ Majburiy hujjatlar")
            st.markdown("""
            1. ✓ Tashqi savdo kontrakti ID raqami (TEDAAT)
            2. ✓ Hisobvaraq-faktura (invoys)
            """)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
            st.markdown("### 📋 Qo'shimcha (zarurat bo'yicha)")
            st.markdown("""
            - Sug'urta hujjatlari
            - Tashish shartnomasi
            - Transport hujjatlari
            - Vositachilik shartnomasi
            - Litsenzion kelishuv
            - Bank to'lov hujjatlari
            """)
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="info-box yellow-box">', unsafe_allow_html=True)
        st.markdown("### ⚠️ Xavf yuqori bo'lganda")
        st.markdown("""
        **Qo'shimcha talab qilinadi:**
        - Jo'natuvchi mamlakat bojxona deklaratsiyasi
        - Uchinchi shaxslar bilan kontraktlar
        - To'lov hisoblari
        
        *Qachon?: Mazkur tovar oxirgi 90 kun ichida olib kirilgan tovardan 
        sezilarli arzon bo'lganda*
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="info-box purple-box">', unsafe_allow_html=True)
        st.markdown("### 📋 2-3 usullar uchun hujjatlar")
        st.markdown("""
        **Majburiy:**
        1. ✓ Aynan bir xil/o'xshash tovar BYD raqami
        2. ✓ 1-usulda qabul qilingan bo'lishi kerak
        3. ✓ So'nggi 90 kun ichida olib kirilgan
        
        **Tuzatishlar uchun (zarur bo'lsa):**
        - Tashish xarajatlari tasdigi
        - Transport farqi hisob-kitobi
        - Yetkazib berish shartlari farqi
        """)
        st.info("💡 Agar farqlar kichik bo'lsa, qo'shimcha hujjatsiz ham mumkin")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="info-box orange-box">', unsafe_allow_html=True)
        st.markdown("### 📋 4-usul uchun hujjatlar")
        st.markdown("""
        **Zaruriy hujjatlar:**
        1. ✓ O'zbekistonda sotish shartnomasi
        2. ✓ Ichki sotish invoysi
        3. ✓ Bojxona to'lovlari to'langanlik hujjati
        4. ✓ Bank to'lov hujjatlari
        5. ✓ Xarajatlarni aks ettiruvchi buxgalterlik hujjatlari
        
        **Qo'shimcha (agar tovar ishlov berilgan bo'lsa):**
        - Ishlov berish shartnomasi
        - Ishlov berish uchun hisob (invoys)
        - Kalkulyatsiya
        """)
        st.warning("⚠️ Hujjatlar yo'qligi BYD elektron bazasi yoki muqobil manbalar bilan almashtirilishi mumkin")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab4:
        st.markdown('<div class="info-box red-box">', unsafe_allow_html=True)
        st.markdown("### 📋 5-usul uchun hujjatlar")
        st.markdown("""
        **Ishlab chiqaruvchidan:**
        1. ✓ Buxgalterlik tijorat hisoblari
        2. ✓ Ishlab chiqarish xarajatlari kalkulyatsiyasi
        3. ✓ Xomashyo va materiallar qiymati
        4. ✓ Umumiy xarajatlar va foyda ma'lumoti
        
        **Qo'shimcha:**
        - Tashish xarajatlari kalkulyatsiyasi
        - Transport hujjatlari
        - Sug'urta polisi
        """)
        st.error("""
        🚫 Muhim talablar:
        - Hujjatlar ishlab chiqargan mamlakatning buxgalterlik standartlariga mos bo'lishi
        - Ma'lumotlar aniq va miqdoriy aniqlangan bo'lishi
        - Hujjat bilan tasdiqlanishi shart
        """)
        st.markdown('</div>', unsafe_allow_html=True)

elif current_slide == "⚡ Eslatmalar":
    st.markdown('<p class="main-title">⚡ Muhim Eslatmalar va Talablar</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box red-box">', unsafe_allow_html=True)
    st.markdown("### 🚫 Qat'iy talablar")
    st.markdown("""
    - ❌ BQD o'chish va bo'yashsiz bo'lishi kerak
    - ❌ Tushunarli va aniq yozilishi shart
    - ❌ Barcha summalar milliy valyutada
    - ❌ ERI bilan tasdiqlanishi majburiy
    - ❌ Hujjatlar rus yoki ingliz tilida (boshqa tillarda tarjima bilan)
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="info-box yellow-box">', unsafe_allow_html=True)
        st.markdown("### ⏰ Muddatlar")
        st.markdown("""
        - **90 kun:** 2-4 usullar uchun
        - **180 kun:** Muqobil (agar 90 da yo'q bo'lsa)
        - **Bir vaqtda:** BYD bilan birga taqdim
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="info-box blue-box">', unsafe_allow_html=True)
        st.markdown("### 💱 Valyuta kursi")
        st.markdown("""
        - **Markaziy Bank kursi**
        - **BYD qabul qilingan kungi**
        - **Qayta hisoblash majburiy**
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box orange-box">', unsafe_allow_html=True)
    st.markdown("### 📝 To'ldirish qoidalari")
    st.markdown("""
    ✅ **To'g'ri:**
    - Grafalar ketma-ket to'ldirilishi
    - Joy yetmasa orqa tomonga yoki qo'shimcha varaqga
    - Har bir ma'lumot tegishli grafada
    - Imzo va muhur aniq
    
    ❌ **Noto'g'ri:**
    - Grafalarni o'tkazib yuborish
    - Ma'lumotlarni aralashtirib yuborish
    - Qo'shimcha varaqsiz bermaslik
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
    st.markdown("### 🔄 Qayta ishlash")
    st.markdown("""
    **Agar kamchiliklar aniqlansa:**
    1. Bojxona organi xabar beradi
    2. Deklaratsiyalovchi shaxs tuzatadi
    3. Qayta taqdim etiladi
    4. Dastlabki tekshiruv o'tkaziladi
    
    **Qabul qilingandan keyin:**
    - BQD BYD bilan bir vaqtda rasmiylashtiriladi
    - BYD raqami BQDga biriktiriladi
    - Bojxona organi belgilarini qo'yadi
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif current_slide == "✅ Xulosa":
    st.markdown('<p class="main-title">✅ Xulosa va Asosiy Xulosalar</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box blue-box">', unsafe_allow_html=True)
    st.markdown("### 🎯 BQD ning asosiy maqsadi")
    st.write("""
    Bojxona qiymat deklaratsiyasi tovarning bojxona qiymatini to'g'ri va shaffof 
    aniqlash, bojxona to'lovlarini hisoblash uchun asos yaratish va halqaro 
    savdo qoidalariga rioya etilishini ta'minlashga xizmat qiladi.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="info-box green-box">', unsafe_allow_html=True)
        st.markdown("### ✅ Asosiy qoidalar")
        st.markdown("""
        1. **Aniqlik** - barcha ma'lumotlar to'g'ri
        2. **To'liqlik** - hamma grafalarda ma'lumot
        3. **Hujjatlilik** - tasdiqlangan hujjatlar
        4. **Vaqtida** - BYD bilan birga
        5. **Elektron** - ERI bilan tasdiq
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="info-box purple-box">', unsafe_allow_html=True)
        st.markdown("### 📊 Usullar ierarxiyasi")
        st.markdown("""
        **1-usul** → Asosiy (90%+)  
        ⬇️ (qo'llab bo'lmasa)  
        **2-usul** → Aynan bir xil tovar  
        ⬇️  
        **3-usul** → O'xshash tovar  
        ⬇️  
        **4-usul** → Ichki sotish narxi  
        ⬇️  
        **5-usul** → Hisoblangan qiymat  
        ⬇️  
        **6-usul** → Zaxira (yuqoridagilar asosida)
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box yellow-box">', unsafe_allow_html=True)
    st.markdown("### 💡 Amaliy maslahatlar")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Tayyorgarlik:**
        - Hujjatlarni oldindan yig'ing
        - Kontrakt shartlarini tekshiring
        - Kurslarga e'tibor bering
        """)
    
    with col2:
        st.markdown("""
        **To'ldirish:**
        - Grafalarni ketma-ket to'ldiring
        - Hisob-kitoblarni tekshiring
        - Summalarni solishtirib ko'ring
        """)
    
    with col3:
        st.markdown("""
        **Tekshirish:**
        - Barcha grafalarda ma'lumot bormi
        - Hujjatlar to'liqmi
        - ERI to'g'rimi
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box orange-box">', unsafe_allow_html=True)
    st.markdown("### 📞 Foydali ma'lumotlar")
    st.markdown("""
    **Qonunchilik asoslari:**
    - O'zbekiston Respublikasi Bojxona kodeksi (303-313-moddalar)
    - "Davlat bojxona xizmati to'g'risida"gi Qonun
    - Iqtisodiyot va moliya vaziri 298-son buyrugʻi (2025-yil 3-noyabr)
    
    **Elektron tizimlar:**
    - TEDAAT (Tovarlarni elektron deklaratsiyalash)
    - Tashqi savdo operatsiyalarining yagona elektron tizimi
    - Bojxona organlari elektron bazasi
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box red-box">', unsafe_allow_html=True)
    st.markdown("### ⚠️ Tez-tez uchraydigan xatolar")
    st.error("""
    ❌ 1-usulni noto'g'ri qo'llash (bog'liqlik e'tiborga olinmagan)  
    ❌ Tuzatishlarni unutish (transport, sug'urta)  
    ❌ Valyuta kursini noto'g'ri qo'llash  
    ❌ Hujjatlarning to'liq emasligi  
    ❌ Grafalarni noto'g'ri to'ldirish  
    ❌ Elektron va qog'oz nusxalarning farqi
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.success("""
    ### 🎓 E'tiboringiz uchun rahmat!
    
    Savollar bormi? Bojxona organlari yoki vakolatli brokerlar bilan maslahatlashing.
    """)
    
    # Qo'shimcha resurslar
    with st.expander("📚 Qo'shimcha resurslar va havolalar"):
        st.markdown("""
        **Rasmiy manbalar:**
        - [Qonunchilik ma'lumotlari milliy bazasi](https://lex.uz)
        - [Davlat bojxona qo'mitasi](https://customs.uz)
        - [Iqtisodiyot va moliya vazirligi](https://mf.uz)
        
        **Yo'riqnomalar:**
        - Bojxona yuk deklaratsiyasini to'ldirish tartibi (2773-raqam)
        - Tovarning bojxona qiymatini aniqlash tartibi (VM 160-son qaror)
        - TIF TN (Tashqi iqtisodiy faoliyat tovar nomenklaturasi)
        
        **Tasniflagichlar:**
        - Valyutalar tasniflagichi
        - Mamlakatlar tasniflagichi
        - Yetkazib berish shartlari (INCOTERMS 2020)
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 2rem;'>
    <p><strong>Bojxona qiymat deklaratsiyasi (BQD)</strong></p>
    <p>O'zbekiston Respublikasi bojxona qonunchiligiga muvofiq</p>
    <p style='font-size: 0.9rem; margin-top: 1rem;'>
        📋 Qonunchilik asosi: Bojxona kodeksi, Iqtisodiyot va moliya vaziri 298-son buyrugʻi
    </p>
    <p style='font-size: 0.8rem; color: #94a3b8;'>
        So'nggi yangilanish: 2025-yil noyabr
    </p>
</div>
""", unsafe_allow_html=True)

# Navigatsiya tugmalari
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    current_index = slides.index(current_slide)
    if current_index > 0:
        if st.button("⬅️ Oldingi", use_container_width=True):
            st.session_state.slide = slides[current_index - 1]
            st.rerun()

with col2:
    st.markdown(f"<p style='text-align: center; color: #64748b;'>Sahifa {current_index + 1} / {len(slides)}</p>", unsafe_allow_html=True)

with col3:
    if current_index < len(slides) - 1:
        if st.button("Keyingi ➡️", use_container_width=True):
            st.session_state.slide = slides[current_index + 1]
            st.rerun()

# Qo'llanma bo'limi
with st.sidebar:
    st.markdown("---")
    st.markdown("### 📖 Qo'llanma")
    
    with st.expander("🔍 BQD turlari"):
        st.markdown("""
        **BQD-1:** 1-usul uchun  
        **BQD-2:** 2-6 usullar uchun
        """)
    
    with st.expander("💡 Maslahatlar"):
        st.markdown("""
        - Hujjatlarni oldindan tayyorlang
        - Grafalarni ketma-ket to'ldiring
        - Hisob-kitoblarni tekshiring
        - Valyuta kursiga e'tibor bering
        """)
    
    with st.expander("⚠️ Ogohlantirishlar"):
        st.markdown("""
        - 1-usulni faqat shartlar bajarilganda qo'llang
        - Barcha hujjatlarni saqlang
        - Muddatlarga rioya qiling
        - ERI ni unutmang
        """)
    
    st.markdown("---")
    st.info("💡 Klaviatura bilan navigatsiya: ← → tugmalari")










