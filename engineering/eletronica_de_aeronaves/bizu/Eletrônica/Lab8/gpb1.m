f = [100000 50000 30000 20000 18000 16000 14000 12000 10000 5000 2000 1000 500 200];
k = [1.048 1.461 1.442 1.176 1.08 0.943 0.909 0.622 0.487 0.167 0.062 0.062 0.041 0.041];

plot(f,k, 'k',  'LineWidth', 3 );
xlabel('Frequência (Hz)'); 
ylabel('Ganho em Tensão');
title('Filtro Passa-Baixa 1 Polo');
grid on;