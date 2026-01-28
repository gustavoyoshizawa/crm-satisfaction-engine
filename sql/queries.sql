-- Clientes em risco
SELECT *
FROM customer_profile
WHERE segmento = 'Risco';

-- Média de dias sem resposta
SELECT AVG(dias_sem_resposta)
FROM customer_profile;

-- Distribuição por segmento
SELECT
  segmento,
  COUNT(*) AS total_clientes,
  AVG(dias_sem_resposta) AS media_dias_sem_resposta
FROM customer_profile
GROUP BY segment
