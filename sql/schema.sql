CREATE DATABASE crm_analytics;
USE crm_analytics;

SELECT * FROM customer_profile;


CREATE VIEW vw_customer_crm AS
SELECT
    cliente_id,
    segmento,
    dias_sem_resposta,
    qtd_interacoes_abertas,
    canal_preferido,
    resumo_ia
FROM customer_profile;

select * from vw_customer_crm;


CREATE USER 'bi_user'@'localhost' IDENTIFIED BY 'bi123';
GRANT SELECT ON crm_analytics.* TO 'bi_user'@'localhost';
FLUSH PRIVILEGES;


SELECT user, host, plugin FROM mysql.user WHERE user = 'bi_user';
SHOW DATABASES;
USE crm_analytics;
SHOW TABLES;
