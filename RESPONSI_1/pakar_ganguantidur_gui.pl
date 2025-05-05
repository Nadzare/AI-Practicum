% Fakta: gejala yang dimiliki setiap gangguan tidur
gangguan(insomnia, G) :- member(G, [g2, g3, g6, g7]).
gangguan(sleep_apnea, G) :- member(G, [g1, g4, g7, g8]).
gangguan(nightmare_disorder, G) :- member(G, [g1, g5, g6]).
gangguan(delayed_sleep_phase, G) :- member(G, [g2, g4, g6]).
gangguan(restless_leg_syndrome, G) :- member(G, [g4, g6, g7, g8]).

% Nama gejala
gejala(g1, 'Sering terbangun tengah malam').
gejala(g2, 'Sulit tidur saat malam').
gejala(g3, 'Bangun terlalu pagi').
gejala(g4, 'Rasa kantuk berlebihan di siang hari').
gejala(g5, 'Sering mimpi buruk').
gejala(g6, 'Kecemasan atau stres').
gejala(g7, 'Mudah lelah saat bangun').
gejala(g8, 'Sakit kepala pagi hari').

% Diagnosa berdasarkan daftar gejala yang dimiliki
diagnosa(GejalaInput, Gangguan) :-
    setof(G, gangguan(Gangguan, G), GejalaGangguan),
    intersection(GejalaInput, GejalaGangguan, Matching),
    length(Matching, Count),
    Count >= 2.  % Ambang batas kemiripan (boleh disesuaikan)

% Menampilkan hasil diagnosa
tampilkan_diagnosa(GejalaInput) :-
    findall(Gangguan, diagnosa(GejalaInput, Gangguan), Hasil),
    write('Gejala yang dimasukkan:'), nl,
    tampilkan_gejala(GejalaInput),
    nl,
    (Hasil \= [] ->
        write('Kemungkinan gangguan tidur yang terdeteksi:'), nl,
        tampilkan_gangguan(Hasil)
    ;
        write('Tidak terdeteksi gangguan tidur berdasarkan gejala tersebut.')
    ).

tampilkan_gejala([]).
tampilkan_gejala([H|T]) :-
    gejala(H, Deskripsi),
    format('- ~w: ~w~n', [H, Deskripsi]),
    tampilkan_gejala(T).

tampilkan_gangguan([]).
tampilkan_gangguan([H|T]) :-
    format('- ~w~n', [H]),
    tampilkan_gangguan(T).
