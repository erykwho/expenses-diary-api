
# Expenses Diary (EXD) API 

Expenses Diary é uma aplicação web que servirá de diário de despesas.

Nesta aplicação, você poderá:

- Registrar suas despesas.
- Consultar suas despesas.
- Gerar relatórios periódicos relacionando seus gastos.
- Gerar gráficos de seus gastos.
- Exportar suas despesas para uma planilha.
- Gerar análises estatísticas de seus gastos.


    Uma despesa conterá:
    - Data
    - Valor
    - Meio de Pagamento
    - Descrição
    - Categoria
    - Arrependimento

Este repositório refere-se à API desta aplicação.


## Endpoints

    /expenses:
        GET /v1/expenses
        POST /v1/expenses
    /expense/{id}:
        GET, PATCH, DELETE
    
    /users:
        GET, POST
    /user/{id}:
        GET, PATCH, DELETE
        
    /payment-origins:
        GET, POST
    /payment-origin/{id}:
        GET, PATCH, DELETE
        
    /categories:
        GET, POST
    /categories:
        PATCH, DELETE

