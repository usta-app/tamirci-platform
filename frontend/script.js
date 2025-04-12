// Kullanıcı Ekleme
document.getElementById('kullanici-form').addEventListener('submit', async function (event) {
    event.preventDefault(); // Formun sayfayı yenilemesini engeller

    const formData = new FormData(event.target);
    const data = {
        isim: formData.get('isim'),
        telefon: formData.get('telefon'),
        email: formData.get('email'),
        arac_turu: formData.get('arac_turu')
    };

    try {
        const response = await fetch('http://127.0.0.1:8002/api/kullanici', {  // Portu 8002'ye güncelledik
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            alert('Kullanıcı başarıyla eklendi!');
            event.target.reset(); // Formu sıfırlar
        } else {
            alert('Bir hata oluştu, lütfen tekrar deneyin.');
        }
    } catch (error) {
        alert('Bir hata oluştu, lütfen tekrar deneyin.');
        console.error(error);
    }
});

// Esnaf Ekleme
document.getElementById('esnaf-form').addEventListener('submit', async function (event) {
    event.preventDefault(); // Formun sayfayı yenilemesini engeller

    const formData = new FormData(event.target);
    const data = {
        dukkan_adi: formData.get('dukkan_adi'),
        telefon: formData.get('telefon'),
        hizmet_alani: formData.get('hizmet_alani'),
        puan: formData.get('puan'),
    };

    try {
        const response = await fetch('http://127.0.0.1:8002/api/esnaf', {  // Portu 8002'ye güncelledik
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            alert('Esnaf başarıyla eklendi!');
            event.target.reset(); // Formu sıfırlar
        } else {
            alert('Bir hata oluştu, lütfen tekrar deneyin.');
        }
    } catch (error) {
        alert('Bir hata oluştu, lütfen tekrar deneyin.');
        console.error(error);
    }
});

