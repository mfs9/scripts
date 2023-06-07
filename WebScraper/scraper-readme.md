# Web Scraping de Notícias

Este script em Python permite extrair notícias de um site específico usando técnicas de Web Scraping. Ele utiliza a biblioteca `requests` para fazer requisições HTTP e a biblioteca `beautifulsoup4` para analisar o HTML da página e extrair os dados desejados.

## Como usar o script

1. Certifique-se de ter o Python instalado em sua máquina. Você pode baixar o Python em [python.org](https://www.python.org).

2. Instale as dependências necessárias executando o seguinte comando no terminal:
   ```
   pip install requests beautifulsoup4
   ```

3. Abra o arquivo `wscraper.py` em um editor de texto ou ambiente de desenvolvimento Python.

4. Na variável `news_url`, defina o URL do site que você deseja extrair as notícias. Por exemplo:
   ```python
   news_url = 'https://g1.globo.com/'
   ```

5. Execute o script executando o seguinte comando no terminal:
   ```
   python wscraper.py
   ```

6. O script irá extrair as notícias do site especificado e exibir o título, a data e o resumo de cada notícia no terminal.

## Personalização

- Você pode personalizar o script para extrair informações adicionais ou diferentes do site. Para fazer isso, você precisará entender a estrutura HTML da página e modificar o código do script de acordo.

- Além disso, você pode salvar os dados extraídos em um arquivo, armazená-los em um banco de dados ou realizar outras operações com eles, de acordo com suas necessidades.

## Limitações

- Este script de Web Scraping é específico para o site usado como exemplo (`https://g1.globo.com/`). Se você deseja extrair notícias de outros sites, é necessário ajustar o código para atender à estrutura HTML desses sites.

- É importante ter cuidado ao realizar Web Scraping e respeitar os termos de uso do site. Alguns sites podem ter políticas específicas sobre a extração de dados automatizada. Verifique as políticas do site antes de usar este script em outros contextos.

## Conclusão

Este script de Web Scraping em Python permite extrair notícias de um site específico, fornecendo os títulos, as datas e os resumos das notícias. Ele pode ser personalizado e adaptado para diferentes sites e finalidades, proporcionando uma maneira eficiente de coletar informações da web.

Espero que este README tenha fornecido as informações necessárias para entender e usar o script. Sinta-se à vontade para modificar e expandir o código de acordo com suas necessidades.