% REKOMENDASI SKINCARE
:- dynamic gejala_pos/1.
:- dynamic gejala_neg/1.

% Jenis rekomendasi skincare (bisa dianggap "penyakit" dalam konteks logika diagnosa)
skincare("Cleanser untuk kulit berminyak berjerawat").
skincare("Moisturizer untuk kulit kering dan kusam").
skincare("Toner untuk kulit kombinasi dan sensitif").
skincare("Serum untuk kulit normal dan cerah").

% Relasi gejala dan skincare
gejala(kulit_berminyak, "Cleanser untuk kulit berminyak berjerawat").
gejala(kulit_berjerawat, "Cleanser untuk kulit berminyak berjerawat").
gejala(kulit_kering, "Moisturizer untuk kulit kering dan kusam").
gejala(kulit_kusam, "Moisturizer untuk kulit kering dan kusam").
gejala(kulit_kombinasi, "Toner untuk kulit kombinasi dan sensitif").
gejala(kulit_sensitif, "Toner untuk kulit kombinasi dan sensitif").
gejala(kulit_normal, "Serum untuk kulit normal dan cerah").
gejala(kulit_cerah, "Serum untuk kulit normal dan cerah").

% Pertanyaan berdasarkan gejala
pertanyaan(kulit_berminyak, Y) :- Y = "Apakah kulit Anda berminyak?".
pertanyaan(kulit_berjerawat, Y) :- Y = "Apakah kulit Anda memiliki jerawat?".
pertanyaan(kulit_kering, Y) :- Y = "Apakah kulit Anda kering?".
pertanyaan(kulit_kusam, Y) :- Y = "Apakah kulit Anda tampak kusam?".
pertanyaan(kulit_kombinasi, Y) :- Y = "Apakah kulit Anda kombinasi (kering dan berminyak)?".
pertanyaan(kulit_sensitif, Y) :- Y = "Apakah kulit Anda sensitif terhadap produk tertentu?".
pertanyaan(kulit_normal, Y) :- Y = "Apakah kulit Anda tergolong normal (tidak bermasalah)?".
pertanyaan(kulit_cerah, Y) :- Y = "Apakah kulit Anda terlihat cerah?".
