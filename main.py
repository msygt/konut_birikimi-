import matplotlib.pyplot as plt
import streamlit as st


st.title('Hakan\'ın Gayrimenkul Yatırımı Hesaplayıcısı')

birikim_aylik = st.number_input('Her ay biriktirdiği miktar (₺)', min_value=0, step=1000)
baslangic_yasi = st.number_input('Başlangıç yaşı', min_value=18, max_value=100, step=1)
emeklilik_yasi = st.number_input('Emeklilik yaşı', min_value=baslangic_yasi + 1, max_value=100, step=1)
daire_fiyati = st.number_input('Rezidans daire fiyatı (₺)', min_value=0)
kira_bedeli = st.number_input('Rezidans daire kira bedeli (₺)', min_value=0)
kredi_yili = st.number_input('Kredi için bölünecek yıl sayısı', min_value=1, step=1)
pesinat_orani = st.number_input('Daire satın alırken ödenecek peşinat yüzdesi (%)', min_value=0, max_value=100, step=5)


def hesaplamalar(birikim_aylik, baslangic_yasi, emeklilik_yasi, daire_fiyati, kira_bedeli, kredi_yili, pesinat_orani):
    toplam_birikim = birikim_aylik * 12 * (emeklilik_yasi - baslangic_yasi)

    ilk_daire_pesinat = daire_fiyati * pesinat_orani / 100

    kalan_kredi = daire_fiyati - ilk_daire_pesinat

    aylık_kredi_odemesi = kalan_kredi / (kredi_yili * 12)

    kira_geliri = kira_bedeli

    adet_daire = 0

    toplam_kira_geliri = 0

    biriken_para = 0

    while biriken_para < toplam_birikim:
        adet_daire += 1
        biriken_para += ilk_daire_pesinat
        toplam_kira_geliri += kira_geliri
        biriken_para += kira_geliri * 12 * (emeklilik_yasi - baslangic_yasi - adet_daire)
        biriken_para -= aylık_kredi_odemesi * 12 * (emeklilik_yasi - baslangic_yasi - adet_daire)

    return {'adet_daire': adet_daire, 'toplam_kira_geliri': toplam_kira_geliri}

if st.button('Hesaplama'):
    sonuclar = hesaplamalar(birikim_aylik, baslangic_yasi, emeklilik_yasi, daire_fiyati, kira_bedeli, kredi_yili, pesinat_orani)
    st.write('Hakan emeklilik yaşına kadar toplamda {} adet daire alabilir ve toplam kira geliri {} olur.'.format(sonuclar['adet_daire'], sonuclar['toplam_kira_geliri']))