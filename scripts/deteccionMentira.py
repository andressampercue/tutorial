#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import collections
import pandas as pd
import numpy as np
import rospy
from std_msgs.msg import String
from tutorial.srv import DeteccionMentira,DeteccionMentiraResponse
import pandas as pd
import pickle
from datetime import datetime

def escribirArchivo(texto):
    path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'auditoria.txt'))    
    path  = path[0:path.find('scripts')]+ 'src/auditoria.txt'    
    with open(path, 'a') as f:
        f.write(str(texto)+'\n')
class Liwc():
    
    """
    Class for the Linguistic Inquiry and Word Count (LIWC) dictionairy.
    The dictionary files are proprietary and can be obtained by liwc.net
    """

    def __init__(self, filepath):
        """
        :param filepath: path to the LIWC .dic file.
        """
        self.categories, self.lexicon = self._load_dict_file(filepath)
        self._trie = self._build_char_trie(self.lexicon)

    def search(self, word):
        """
        Search a word in the liwc dictionairy.

        :param word:
        :return: a list of the liwc categories the word belongs.
                 an empty list if the word is not found in the dictionary.
        """    
        number = self._check_search_trie(self._trie, word)    
        
        #print(word)
        
        if (number==2):
            return self._search_trie(self._trie, word)            
        elif (number==1):
            first_list = self._search_trie(self._trie, word)            
            second_list = self._modificado_search_trie(self._trie, word) 

            in_first = set(first_list)
            in_second = set(second_list)

            in_second_but_not_in_first = in_second - in_first

            unidito = first_list + list(in_second_but_not_in_first)
            #print("unidito ",unidito)  # Prints [1, 2, 2, 5, 9, 7]

            #print ("*************",word,first_list)
            #print ("*************",word,second_list)
            #print (first_list)
            #print (second_list)
            return unidito
        elif (number==3):
            return []


    def parse(self, tokens):
        """
        Parses a document and extracts raw counts of words that fall into the
        various LIWC categories.

        :param tokens: a list of tokens, a tokeniSed document
        :return: a counter with the linguistic categories found in the doc,
                and the raw count of words that fall in each category.
        """
        cat_counter = collections.Counter()
        
        for token in tokens:
            # Find in which categories this token falls, if any
            simbolos = ['¿','?','.','.',';',':','¡','!',',']
            
            for simbolo in simbolos:
                token = token.replace(simbolo,'')
            
            cats = self.search(token)            
            
            for cat in cats:                
                cat_counter[cat] += 1
                

        return cat_counter

    def _load_dict_file(self, filepath):
        liwc_file = open(filepath)

        # Key, category dict
        categories = {}

        # Word, cat_name dict
        lexicon = {}

        # '%' signals a change in the .dic file.
        # (0-1) Cats, ids
        # (>1) Words, cat_ids
        percent_sign_count = 0

        for line in liwc_file:
            stp = line.strip()

            if stp:
                parts = stp.split('\t')

                if parts[0] == '%':
                    percent_sign_count += 1
                else:
                    # If the percent sign counter equals 1, parse the LIWC
                    # categories
                    if percent_sign_count == 1:
                        categories[parts[0]] = parts[1]
                    # Else, parse lexicon
                    else:
                        lexicon[parts[0]] = [categories[cat_id]
                                             for cat_id in parts[1:]]

        return categories, lexicon

    @staticmethod
    def _build_char_trie(lexicon):
        """
        Builds a char trie, to cater for wildcard ('*') matches.
        """
        trie = {}
        for pattern, cat_names in lexicon.items():
            cursor = trie
            for char in pattern:
                if char == '*':
                    cursor['*'] = cat_names
                    break

                if char not in cursor:
                    cursor[char] = {}

                cursor = cursor[char]

            # $ signifies end of token
            cursor['$'] = cat_names

        return trie

    @staticmethod
    def _search_trie(trie, token, i=0):
        """
        Search the given char trie for paths that match the token.
        """
        #print("search", token)
        if '*' in trie:    
            #print(trie['*'])        
            return trie['*']
        elif '$' in trie and i == len(token):
            #print ("aall")
            return trie['$']
        
        elif i < len(token):
            char = token[i]
            if char in trie:
                return Liwc._search_trie(trie[char], token, i + 1)
        #elif '*' in trie:            
        #    #print("eeee")
        #    return trie['*']
        return []

    @staticmethod
    def _check_search_trie(trie, token, i=0):
        """
        Search the given char trie for paths that match the token.
        """
        #print("search", token)
        if '*' in trie:    
            return 1
        elif '$' in trie and i == len(token):
            return 2
        
        elif i < len(token):
            char = token[i]
            if char in trie:
                return Liwc._check_search_trie(trie[char], token, i + 1)
        #elif '*' in trie:            
        #    #print("eeee")
        #    return trie['*']
        return 3
    
    @staticmethod
    def _modificado_search_trie(trie, token, i=0):
        """
        Search the given char trie for paths that match the token.
        """
        #print("search", token)
        
        if '$' in trie and i == len(token):
            #print ("aall")
            return trie['$']
        
        elif i < len(token):
            char = token[i]
            if char in trie:
                return Liwc._modificado_search_trie(trie[char], token, i + 1)
        #elif '*' in trie:            
        #    #print("eeee")
        #    return trie['*']
        return []

        
    @staticmethod
    def contarPalabras(linea):
        simbolos = ['¿','?','.','.',';',':','¡','!']
        numpalabras = 0
        
            
        for simbolo in simbolos:
            linea = linea.replace(simbolo,' ')
        palabras = linea.split()
        for palabra in palabras:            
            numpalabras += 1                    
        print('Principal El texto contiene %s palabras' %numpalabras)
        return numpalabras


    def cuentaNoPresente(self, tokens):
        """
        Parses a document and extracts raw counts of words that fall into the
        various LIWC categories.

        :param tokens: a list of tokens, a tokeniSed document
        :return: a counter with the linguistic categories found in the doc,
                and the raw count of words that fall in each category.
        """
        simbolos = ['¿','?','.','.',';',':','¡','!',',']
        numpalabras = 0
        cat_counter = collections.Counter()
        sumaNodiccionario = 0
        for token in tokens:
            for simbolo in simbolos:
                token = token.replace(simbolo,'')
                # Find in which categories this token falls, if any
            cats = self.search(token)
            if (len(cats)==0):                
                sumaNodiccionario +=1
            
        return sumaNodiccionario

    def cuentaMayorDeSeisLetras(self, tokens):
        """
        Parses a document and extracts raw counts of words that fall into the
        various LIWC categories.

        :param tokens: a list of tokens, a tokeniSed document
        :return: a counter with the linguistic categories found in the doc,
                and the raw count of words that fall in each category.
        """
        simbolos = ['¿','?','.','.',';',':','¡','!',',']
        sumaMayorSeis = 0
        for token in tokens:
            for simbolo in simbolos:
                token = token.replace(simbolo,'')
                # Find in which categories this token falls, if any
            if (len(token)>6):                
                sumaMayorSeis +=1
            
        return sumaMayorSeis


# Replace with the path of a liwc (.dic) file
LIWC_FILEPATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'Spanish_LIWC2007_Dictionary.dic'))

MODEL_FILEPATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'ramdomForestTotal'))

CATEGORIES_FILEPATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'export_dataframe.csv'))

def deteccion_mentira(req):
    print("Ingresa de peticion ", req.analizar)
    liwc = Liwc(LIWC_FILEPATH)

    #print(liwc.search('caminaba'))
    #respuesta = "mi recuerdo mas vivido son los viajes familiares que he realizado, actualmente por cuestiones de la pandemia y por cuestiones de que ya todos somos adultos, ya no los hago, pero era un momento en el que podia compartir con toda mi familia nos olvidabamos de todas nuestras responsabilidades en el pais y simplemente disfrutabamos de nuestra compañía."
    
    respuesta = req.analizar#se asigna la peticion a la variable de entrada del proceso

    numeroPalabras = liwc.contarPalabras(respuesta)
    varWC = numeroPalabras#total de palabras presentes
    counters = liwc.parse(respuesta.split(' '))
    noPresente = liwc.cuentaNoPresente(respuesta.split(' '))
    varSixltr = liwc.cuentaMayorDeSeisLetras(respuesta.split(' '))
    varSixltr = round(((varSixltr/numeroPalabras)*100),2)#porcentaje de palabras con mas de 6 letras
    varDic = round((((numeroPalabras-noPresente)*100)/numeroPalabras),2)#porcentaje de palabras que no estuvieron en el diccionario

    varPeriod = round (((respuesta.count(".")/numeroPalabras)*100),2)
    varComma = round(((respuesta.count(",")/numeroPalabras)*100),2)
    varColon = round(((respuesta.count(":")/numeroPalabras)*100),2)
    varSemiColon = round(((respuesta.count(";")/numeroPalabras)*100),2)
    varQMark = round(((respuesta.count("?")/numeroPalabras)*100),2)
    varExclam = round(((respuesta.count("!")/numeroPalabras)*100),2)
    varDash = round(((respuesta.count("-")/numeroPalabras)*100),2)
    varQuote = round(((respuesta.count('"')/numeroPalabras)*100),2)
    varApostro = round(((respuesta.count('"')/numeroPalabras)*100),2)
    varParenth = round(((respuesta.count("'")/numeroPalabras)*100),2)
    varOtherP = 0
    varAllPunc = varPeriod+varComma+varColon+varSemiColon+varQMark+varExclam+varDash+varQuote+varApostro+varParenth+varOtherP 
    varAllPunc = round(varAllPunc,1)
    varClass=0

    #print (varAllPunc," - ", varPeriod," - ", varComma, " - ",varColon, " - ",varSemiColon, " - ",varQMark," - ", varExclam," - ", varDash," - ",varQuote)
    print("Crea las columnas 000")
    for ele in counters:
        counters[ele]= round(((counters[ele]/numeroPalabras)*100),2)

    #for ele in counters:
    #    print(ele,counters[ele])


    dataFrame = pd.DataFrame([counters])
    #df = pd.DataFrame.from_dict(counters).reset_index()
    
    varSegment=1
    varWPS=1#words per sentence
    #print (counters)
    #print (varDic)
    #print (varSixltr)
    #print (varWC)

    arry=['response.txt','1',varWC,varWC,varSixltr,varDic]
    #colm=['Filename','Segment','WC','WPS','Sixltr','Ddic','Funct','TotPron','PronPer','Yo','Nosotro','TuUtd','ElElla','Ellos'
    # ,'PronImp','Articulo','Verbos','VerbAux','Adverb','Prepos','Conjunc','Negacio','Cuantif','Numeros','Social','Familia',
    # 'Amigos','Afect','EmoPos','EmoNeg','Ansiedad','Enfado','Triste','Insight','Causa','Discrep','Tentat','Certeza','Excl','
    # Percept','Ver','Oir','Sentir','Biolog','Cuerpo','Salud','Sexual','Ingerir','Espacio','Tiempo','Trabajo','Logro','Placer',
    # 'Hogar','Dinero','Relig','Muerte','AllPunc','Period','Comma','Colon','SemiC','QMark','Exclam','Dash','Quote','Apostro',
    # 'Parenth','OtherP','Class']
    colm=['Filename','Segment','WC','WPS','Sixltr','Dic','Nosotro','ElElla','Ellos','Verbos','Pasado','Presente'
    ,'Cuantif','Numeros','verbYO','verbTU','verbNOS','verbEL','verbELLOS','VosUtds','Social','Humanos','EmoPos'
    ,'EmoNeg','Insight','Percept','Oir','Sentir','Tiempo','AllPunc','Period','Comma','Colon','SemiC','QMark','Exclam'
    ,'Dash','Quote','Apostro','Parenth','OtherP','Class']
    

    i=0    
    valor=0
    for co in colm:
        if (i>5):
            if (i<29):#57
                flag=00
                for ele in counters:
                    comp=co
                    comp1=ele
                    #print (comp,comp1)
                    if (co==ele):
                        if (flag==0):
                            flag=1
                            valor=counters[ele]
                            #print(ele,counters[ele])                
                if (flag==1):
                    arry.append(valor)
                else:
                    arry.append(0)
                i=i+1
            else:
             i=i+1   
        else:
            i=i+1
    #print(arry)      
    print("Crea las columnas 111")
    #cargamos los ultimos valores calculados  
    arry.append(varAllPunc)
    arry.append(varPeriod)
    arry.append(varComma)
    arry.append(varColon)    
    arry.append(varSemiColon)
    arry.append(varQMark)
    arry.append(varExclam)
    arry.append(varDash)
    arry.append(varQuote)
    arry.append(varApostro)
    arry.append(varParenth)
    arry.append(varOtherP)
    arry.append(varClass)


    df5 = pd.DataFrame(np.array([arry]),
                   columns=colm)

    df5.to_csv (CATEGORIES_FILEPATH, index = False, header=True)
    print("tamanio " ,len(colm))
    #print (df5.iloc[1:,57])

    #------------------------------------------------------------------------
    #dfa = pd.read_csv("LIWC2015Total2Only2.csv")
    x_testA = df5.iloc[:,2:-1]
    y_testA = df5.iloc[:,-1]
    print (x_testA)
    print (y_testA)


    

    	
    with open(MODEL_FILEPATH, "rb") as f:
    	loaded = pickle.load(f, encoding='iso-8859-1')
	
    respuesta = loaded.predict(x_testA)
    print (respuesta[0])

    
    if (respuesta==0):
        escribirArchivo("Nodo Detector mentiras responde>: Es mentira "+ " - " + str(datetime.today()))
        print ("Nodo Detector mentiras responde>: Es mentira ")    
    else:#si es verdad la respuesta es 1
        print ("Nodo Detector mentiras responde>: Es Verdad ")    
        escribirArchivo("Nodo Detector mentiras responde>: Es verdad "+ " - " + str(datetime.today()))
    #------------------------------------------------------------------------
    return respuesta[0]#devolvemos la respuesta de tipo int

def deteccion_mentira_server():
    #bot.storage.drop()
    rospy.init_node('detectarMentira_server')
    s = rospy.Service('detectartMentira', DeteccionMentira, deteccion_mentira)
    print(">>>>>>>>>>>>>>>>>>>> Listo nodo detector mentira. <<<<<<<<<<<<<<<<<<<<<<<")
    rospy.spin()


if __name__ == "__main__":
    deteccion_mentira_server()