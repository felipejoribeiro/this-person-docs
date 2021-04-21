% Alfredo Custódio Lima Cota
% Lista 2 - Mecatrônica
clc;
close all;
clear all;
%% Questão 1

tensao_hp = [0.00318202 0.269626 0.435228 0.652356 0.891221 1.054856 1.229659 1.461453 1.681190 1.850791 1.981107];
tensao_minipa = [0.0031 0.2695 0.4351 0.6523 0.8911 1.0547 1.2307 1.4625 1.6830 1.8521 1.9803];

% pelo polinômio interpolador
k = polyfit(tensao_hp,tensao_minipa,1);
a_k = k(1);
b_k = k(2);
ybest =  polyval(k,tensao_hp);
somadist = sum((tensao_minipa-ybest).^2); 
dr = (tensao_minipa-ybest);
figure(1)
plot(tensao_hp,ybest,tensao_hp,tensao_minipa,'or');
grid on
figure(2)
stem(tensao_hp,dr);
grid on

% pela função regress
n = length(tensao_hp);
X = [ones(n,1) tensao_hp'];
[pr, g, resi] =  regress(tensao_minipa',X);
figure(3)
y2 = pr(1)+ pr(2)*tensao_hp;
plot(tensao_hp,y2,tensao_hp,tensao_minipa,'or');
grid on
figure(4)
stem(tensao_hp,resi);
grid on

%% Questão 2

massa_1 = [0 0.490 1.474 2.457 4.439 6.959 11.997];
massa_2 = [0.580 1.070 2.054 3.040 5.022 7.542 12.58];
tensao_1_1 = [-0.0351805 -0.1014555 -0.237981 -0.377301 -0.656438 -1.008969 -1.710207];
tensao_2_1 = [-0.0332095 -0.1002115 -0.243285 -0.377443 -0.659317 -1.008895 -1.710207];
tensao_1_2 = [ 0.0766392 0.1261190 0.262307 0.399873 0.679279 1.032813 1.738543];
tensao_2_2 = [ 0.731370 0.1283680 0.266097 0.405097 0.680896 1.033632 1.738543];

% para carga
m_1 = [massa_1 massa_1];
t_1 = [tensao_1_1 tensao_2_1];
n_c = length(m_1);
X_c = [ones(n_c,1) m_1'];
[c, h, resi_1] =  regress(t_1',X_c);
figure(5)
y3 = c(1) + c(2)*m_1;
plot(m_1,y3,m_1,t_1,'or');
grid on
figure(6)
stem(m_1,resi_1);
grid on

% para descarga
m_2 = [massa_2 massa_2];
t_2 = [tensao_1_2 tensao_2_2];
n_t = length(m_2);
X_t = [ones(n_t,1) m_2'];
[t, i, resi_2] =  regress(t_2',X_t);
figure(7)
y4 = t(1)+ t(2)*m_2;
plot(m_2,y4,m_2,t_2,'or');
grid on
figure(8)
stem(m_2,resi_2);
grid on

% histerese
y5 = c(1) + c(2)*massa_1;
figure(9)
plot(massa_1,y5,'-b',massa_1,tensao_1_1,'-r',massa_1,tensao_2_1,'-y');
grid on
y6 = t(1) + t(2)*massa_2;
figure(10)
plot(massa_2,y6,'-b',massa_2,tensao_1_2,'-r',massa_2,tensao_2_2,'-y');
grid on

% sensibilidade estática
disp('Sensibilidade estática');
Se = c(2);
disp(Se);