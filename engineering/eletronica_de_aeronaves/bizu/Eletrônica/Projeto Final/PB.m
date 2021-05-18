f = [50 100 200 500 1000 1500 1750 2000 2250 2500 3000 4000 6000 10000];
k = [1.967 1.96 1.967 2.03 2.16 2.26 2.2 2.08 1.83 1.59 1.13 0.64 0.29 0.1];

plot(f,k, 'k',  'LineWidth', 3 );
xlabel('Frequência (Hz)'); 
ylabel('Ganho em Tensão');
title('Filtro Passa-Baixa');
grid on;