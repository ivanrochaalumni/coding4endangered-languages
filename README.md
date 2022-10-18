# coding4natural-languages
This repository is to store some scripts for natural languages

# **Introduction//Introdução**
This code will extract data from a Lift (lexical interchange format) file from FieldWork Language Explorer - SIL (FLEX) and convert it into CSV (Comma-Separeted Values) file. The code is built to extract the **Entries** (vernacular language), Pronunciation (phonetic/phonologic), Glosses (from 2 analyses languages), **Grammmatical information**, example of use (vernacular language), translation into the first Analysis language, and translation into the second Analysis language.  **IMPORTANT**:  your FLEX database must have NO EMPTY FIELD in both columns **HEADWORD**(entries) and **GRAMMATICAL INFO (full)**.


# **Description of Libraries and Modules//Descrição das bibliotecas e Módulos**
This block imports the libraries and modules needed! **xml.etree.ElementTree** module allows us format XML data in a tree structure. Element type allows storage of these data in memory, showing the following properties: tag, attributes, text string, tail string, and child elements. The **Pandas** library allows us to read the data parsed by **xml.etree.ElementTree** module as a DataFrame. This library is also built-in functions and methods that convert the data frame into CSV files.

Este bloco importa as bibliotecas e módulos necessários. O módulo xml.etree.ElementTree nos permite formatar dados XML em estruturas arbóreas. Entidades do tipo *Element* permitem o armazenamento desses dados na memória, apresentando as seguintes propriedades: tag, attributes, text string, tail string e child elements.

# **Inputs from users//Interação com usuários**
1. **INSTRUCTION 1:**Paste here the full path of your Lift file (assumed you
uploaded it to **Colab** and copied the path). Note: If you are running this code from your computer you should put the script lift2csv.py and your Lift file into the same folder; In this case you should type the name and extension .lift in this input field.//Cole o caminho completo do seu arquivo (assumimos que você tenha upload isso no **Colab**). **Note:** Se você estiver rodando o código a partir de seu computador, coloque o script e o arquivo Lift na mesma pasta; então digite o nome do arquivo Lift completo (com a expensão .lift).
2. **INSTRUCTION 2:** Type the code of the vernacular language as defined in your FLEX database (exs: Sena **seh**, Portuguese **pt**, English **en**).**//**Digite o código da língua vernácula, aquela com a qual você está trabalhando.

# **Em construção**
