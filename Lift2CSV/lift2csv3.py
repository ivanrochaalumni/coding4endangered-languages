import xml.etree.ElementTree as ET
import pandas as pd


#Nome do arquivo Lift
fileName = input("INSTRUÇÃO 1: Digite o nome do seu arquivo Lift, ex., lift.lif: ")

#Checar a existência de entrada de difinição
definition_entry = int(input("INSTRUÇÃO 2: Se tiver um campo DEFINIÇÃO no léxico digite: 1, se não tiver: 0: "))
if definition_entry == 1:
    def_lang_code = input("INSTRUÇÃO 2.1: Digite o código ISO da língua de definição, ex. português (pt): ")

#Digite o código da língua vernacular, ex.: Karitiana (ktn), português (pt)
vernacular_langCode = input("INSTRUÇÃO 3: Digite o código da língua vernacular como definida no FLEX: ")

#Código da primeira língua de análise
analysis1_langCode = input("INSTRUÇÃO 4: Digite o código da primeira língua de análise como definida no FLEX: ")

#Checar se há uma segunda língua de análise
analysis_lang2 = int(input("INSTRUÇÃO 5: Se tiver a segunda língua de análise digite: 1, se não tiver digite:0 : "))
if analysis_lang2 == 1:
    analysis2_langCode = input("INSTRUÇÃO 5.1: Digite o código da segunda língua de análise como definida no FLEX: ")



tree = ET.parse(fileName)
root = tree.getroot()
dictionary = []

for entry in root.findall(".//entry"):
    form = entry.find(".//lexical-unit/form")
    form_text = "".join(form.itertext())
    trait_value = entry.find(".//trait").get("value")
    pronunciation = entry.find(".//pronunciation")
    try:
        grammatical_info = entry.find(".//sense/grammatical-info").get("value")
    except:
        if AttributeError:
            grammatical_info = ''

    if pronunciation:
        pronunciation_text = "".join(pronunciation.itertext()).strip()
    else:
        pronunciation_text = ''

    translation_pt = entry.find(".//gloss[@lang='{0}']".format(analysis1_langCode))
    if translation_pt:
        translation_pt_text = "".join(translation_pt.itertext()).strip()
    else:
        translation_pt_text = ''
    if analysis_lang2 == 1:
        translation_en = entry.find(".//gloss[@lang='{0}']".format(analysis2_langCode))
        if translation_en:
            translation_en_text = "".join(translation_en.itertext()).strip()
        else:
            translation_en_text = ''

    example = entry.find(".//example/form[@lang='{0}']".format(vernacular_langCode))
    if example:
        example_text = "".join(example.itertext()).strip()

    else:
        example_text = ''

    example_translationA = entry.find(".//example/translation/form[@lang='{0}']".format(analysis1_langCode))
    if example_translationA:
        example_translationA_text = "".join(example_translationA.itertext()).strip()
    else:
        example_translationA_text = ''

    if analysis_lang2 == 1:
        example_translationB = entry.find(".//example/translation/form[@lang='{0}']".format(analysis2_langCode))
        if example_translationB:
            example_translationB_text = "".join(example_translationB.itertext()).strip()
        else:
            example_translationB_text = ''
    if definition_entry == 1:
        definition = entry.find(".//definition/form[@lang='{0}']".format(def_lang_code))
        if definition:
            definition_text = "".join(definition.itertext()).strip()
        else:
            definition_text = ''
    else: definition_text = ''

    if trait_value == "stem" or trait_value == "root":
        item = {}

        item['entry'] = form_text.strip()
        item['pronunciation'] = pronunciation_text.strip()
        item['gloss_A'] = translation_pt_text.strip()
        if analysis_lang2 == 1:
            item['gloss_B'] = translation_en_text.strip()
        item['grammatical-info'] = grammatical_info.strip()
        item['definition'] = definition_text.strip()
        item['example'] = example_text.strip()
        item['example_analysis1'] = example_translationA_text.strip()
        if analysis_lang2 == 1:
            item['example_anaysis2'] = example_translationB_text.strip()

        dictionary.append(item)  # Append item into the array called dictionary.

        dictionary = sorted(dictionary,
                            key=lambda i: i['entry'].lower())  # Organizing the dictionary in an alphabetic order.

"""This will read the dictionary as Data Frame. Then converted it into CSV. And then create your csv file."""
df = pd.DataFrame.from_dict(dictionary)
df.to_csv(r'Output/myOutput.tsv', index=False, header=True, sep='\t')