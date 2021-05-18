f = [200 500 1000 1500 2000 2500 3000 4000 6000 8000 10000 15000 20000 30000];
k = [0.0645 0.129 0.3548 0.7419 1.333 1.83 2.1 2.16 2.06 1.98 1.98 1.7 1.3 0.79];

plot(f,k, 'k',  'LineWidth', 3 );
xlabel('Frequência (Hz)'); 
ylabel('Ganho em Tensão');
title('Filtro Passa-Alta');
grid on;