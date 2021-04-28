f = [200 500 1000 1500 2000 2500 3000 4000 6000 8000 10000 15000 20000 30000];
k2 = [0.065 0.129 0.355 0.742 1.33 1.833 2.1 2.161 2.065 1.968 1.968 1.7 1.3 1.1];

g = plot(f,k2, 'k',  'LineWidth', 3 );

xlabel('Frequência (Hz)'); 
ylabel('Ganho em Tensão');
title('Filtro Passa-Alta');
grid on;