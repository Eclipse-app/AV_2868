import streamlit as st

# ==================== SAHIFA SOZLAMALARI ====================
st.set_page_config(
    page_title="Oʻzbekiston Respublikasi bojxona hududiga olib kiriladigan tovarlarning bojxona qiymati deklaratsiyasini toʻldirish tartibi",
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
st.sidebar.title("BQD Taqdimoti")
st.sidebar.markdown("**Bojxona Qiymat Deklaratsiyasi**")
st.sidebar.markdown("---")

slides = [
    "1-bob. Umumiy qoidalar",
    "BQD Turlari",
    "Taqdim Shakllari",
    "BQD-1 (1-usul)",
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

if title == "1-bob. Umumiy qoidalar":
    st.markdown('<h1 class="main-title">Bojxona Qiymat Deklaratsiyasi (BQD)</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">O‘zbekiston Respublikasi bojxona hududiga olib kiriladigan tovarlar uchun majburiy hujjat</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Uzbekistan.png", width=150)
    
    st.markdown("""
    <div class="card card-blue">
        <h3>📖 BQD nima?</h3>
        <p><strong>Bojxona Qiymat Deklaratsiyasi (BQD)</strong> — BQD — bojxona yuk deklaratsiyasining (bundan buyon matnda BYD deb yuritiladi) ajralmas qismi boʻlib, tovarning bojxona qiymati toʻgʻrisidagi maʼlumotlar koʻrsatilgan va deklarant yoki bojxona brokeri tomonidan bojxona organiga BYD bilan bir paytda topshiriladigan hujjat;</p>
        <p><strong>Qonuniy asos:</strong> AV <strong> 2868 </strong></p>
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













