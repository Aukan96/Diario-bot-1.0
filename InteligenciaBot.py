#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import re 
import random
import sys
import unicodedata
import my_conexion
sys.stdout.encoding 
'UTF-8'


# PROCESAR MENSAJE DE USUARIO

def generarRespuesta(mensaje, STATES, username):

    message_=sinAcentos(mensaje)
   
    ans=''
    vez = STATES['vez']
    print(message_)

    SALUDO = re.compile('^(h|H)ola|HOLA|(Q|q)u(e|é)\stal|QU(É|E)\sTAL|((B|b)uenas)|BUENAS|(Q|q)u(e|é)\sonda|QU(E|É)\sONDA|(H|h)ello|HELLO|(H|h)i|HI|(Q|q)iubo|QUIUBO|(S|s)aludos|SALUDOS|(B|b)uenos\sd(i|í)as|BUENOS\sD(I|Í)AS($|.*)');
    SALUDO_MATCH = re.match(SALUDO,message_)
    if SALUDO_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nHola, soy DiarioBot, me encantaria platicar contigo..."
	if ev == 2:
        	ans =ans + "\nHola, yo soy tu diario personal..."
	if ev == 3:
        	ans =ans + "\nHola, vamos a platicar..."



    SENTIMIENTO = re.compile('(.*|^)((E|e)stoy|(M|m)e\s(fue|(S|s)iento)|puse|sent(i|í))(.*|(M|m)uy)\s((F|f)el(i\í)z|(C|c)ontent(o|a)|(A|a)legre|(B|b)ien)($|.*)');
    SENTIMIENTO_MATCH = re.match(SENTIMIENTO,message_)
    if SENTIMIENTO_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nMe alegra que te sientas así, espero todos los días te sientas de esa manera, ¿Que más pasó?..."
	if ev == 2:
        	ans =ans + "\nQue bueno que estes así, ¿Que mas pasó?..."
	if ev == 3:
        	ans =ans + "\nMuy bien, que siempre sea así, ¿Que mas pasó?..."
        
    SENTIMIENTO_1 = re.compile('(.*|^)((E|e)stoy|(M|m)e\s(fue|(S|s)iento)|puse|sent(i|í))(.*|(M|m)uy)\s((T|t)riste|(M|m)al|(I|i)nfel(i|í)z|(D|d)ecaid(o|a))($|.*)');
    SENTIMIENTO_MATCH = re.match(SENTIMIENTO_1,message_)
    if SENTIMIENTO_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nNo me gusta que te sientas asi animo, Cuenta me más..."
	if ev == 2:
        	ans =ans + "\nQue mal en serio, Cuenta me más..."
	if ev == 3:
        	ans =ans + "\nNo te preocupes, se que estaras mejor mañana, Cuenta me más..."
    
    NO_MAMA = re.compile('(.*|^)(fallecio|murio|no\stengo)(|\smi)\smam(a|á)($|.*)');
    NO_MATCH = re.match(NO_MAMA,message_)
    if NO_MATCH:
        my_conexion.cambiar_estado('mama',username)
	ev = random.randint(1, 2)
	if ev == 1:
            STATES['mama'] = True
            ans =ans + "\nLo siento mucho, se que es algo demaciado doloroso, ¿Quieres seguir platicando?..."
	if ev == 2:
            STATES['mama'] = True
            ans =ans + "\nQue fuerte, lo siento ¿Quieres seguir platicando?..."

    NO_MAMA = re.compile('(.*|^)mi\smam(a|á)\s(fallecio|murio)($|.*)');
    NO_MATCH = re.match(NO_MAMA,message_)
    if NO_MATCH:
        my_conexion.cambiar_estado('mama',username)
	ev = random.randint(1, 2)
	if ev == 1:
            STATES['mama'] = True
            ans =ans + "\nLo siento mucho, se que es algo demaciado doloroso, ¿Quieres seguir platicando?..."
	if ev == 2:
            STATES['mama'] = True
            ans =ans + "\nQue fuerte, lo siento ¿Quieres seguir platicando?..."

    NO_PAPA = re.compile('(.*|^)(falleci(o|ó)|muri(o|ó)|no\stengo)(|\smi)\spap(a|á)($|.*)');
    NO_MATCH = re.match(NO_PAPA,message_)
    if NO_MATCH:
        my_conexion.cambiar_estado('papa',username)
	ev = random.randint(1, 2)
	if ev == 1:
            STATES['papa'] = True
            ans =ans + "\nLo siento mucho, se que es algo demaciado doloroso, ¿Quieres seguir platicando?..."
	if ev == 2:
            STATES['papa'] = True
            ans =ans + "\nQue fuerte, lo siento ¿Quieres seguir platicando?..."

    NO_PAPA = re.compile('(.*|^)mi\spap(a|á)\s(fallecio|murio)($|.*)');
    NO_MATCH = re.match(NO_PAPA,message_)
    if NO_MATCH:
        my_conexion.cambiar_estado('papa',username)
	ev = random.randint(1, 2)
	if ev == 1:
            STATES['papa'] = True
            ans =ans + "\nLo siento mucho, se que es algo demaciado doloroso, ¿Quieres seguir platicando?..."
	if ev == 2:
            STATES['papa'] = True
            ans =ans + "\nQue fuerte, lo siento ¿Quieres seguir platicando?..."
            
    NO_HERMA = re.compile('(.*|^)(fallecio|murio|no\stengo)(|\smi)\sherman(o|a)($|.*)');
    NO_MATCH = re.match(NO_PAPA,message_)
    if NO_MATCH: 
        my_conexion.cambiar_estado('hermano',username)
	ev = random.randint(1, 2)
	if ev == 1:
            STATES['hermano'] = True
            ans =ans + "\nLo siento mucho, se que es algo demaciado doloroso, ¿Quieres seguir platicando?..."
	if ev == 2:
            STATES['hermano'] = True
            ans =ans + "\nQue fuerte, lo siento ¿Quieres seguir platicando?..."

    NO_HERMA = re.compile('(.*|^)mi\sherman(o|a)\s(fallecio|murio)($|.*)');
    NO_MATCH = re.match(NO_PAPA,message_)
    if NO_MATCH:
        my_conexion.cambiar_estado('hermano',username)
	ev = random.randint(1, 2)
	if ev == 1:
            STATES['hermano'] = True
            ans =ans + "\nLo siento mucho, se que es algo demaciado doloroso, ¿Quieres seguir platicando?..."
	if ev == 2:
            STATES['hermano'] = True
            ans =ans + "\nQue fuerte, lo siento ¿Quieres seguir platicando?..."

    NO_MAS = re.compile('(.*|^)(fallecio|murio|no\stengo)(|\smi)\s(mascota|perro|gato|pajaro|pez|rana|tortuga|iguana)($|.*)');
    NO_MATCH = re.match(NO_MAS,message_)
    if NO_MATCH:
        my_conexion.cambiar_estado('mascota',username)
	ev = random.randint(1, 2)
	if ev == 1:
            STATES['mascota'] = True
            ans =ans + "\nLo siento mucho, se que es algo demaciado doloroso, ¿Quieres seguir platicando?..."
	if ev == 2:
            STATES['mascota'] = True
            ans =ans + "\nQue fuerte, lo siento ¿Quieres seguir platicando?..."

    NO_MAS = re.compile('(.*|^)mi\s(mascota|perro|gato|pajaro|pez|rana|tortuga|iguana)\s(fallecio|murio)($|.*)');
    NO_MATCH = re.match(NO_MAS,message_)
    if NO_MATCH:
        my_conexion.cambiar_estado('mascota',username)
	ev = random.randint(1, 2)
	if ev == 1:
            STATES['mascota'] = True
            ans =ans + "\nLo siento mucho, se que es algo demaciado doloroso, ¿Quieres seguir platicando?..."
	if ev == 2:
            STATES['mascota'] = True
            ans =ans + "\nQue fuerte, lo siento ¿Quieres seguir platicando?..."

    NO_AMI = re.compile('(.*|^)(fallecio|murio|no\stengo)(|\smi)\smejor amig(o|a)($|.*)');
    NO_MATCH = re.match(NO_AMI,message_)
    if NO_MATCH:
        my_conexion.cambiar_estado('amigo',username)
	ev = random.randint(1, 2)
	if ev == 1:
            STATES['amigo'] = True
            ans =ans + "\nLo siento mucho, se que es algo demaciado doloroso, ¿Quieres seguir platicando?..."
	if ev == 2:
            STATES['amigo'] = True
            ans =ans + "\nQue fuerte, lo siento ¿Quieres seguir platicando?..."

    NO_AMI = re.compile('(.*|^)mi\smejor amig(o|a)\s(fallecio|murio)($|.*)');
    NO_MATCH = re.match(NO_AMI,message_)
    if NO_MATCH:
        my_conexion.cambiar_estado('amigo',username)
	ev = random.randint(1, 2)
	if ev == 1:
            STATES['amigo'] = True
            ans =ans + "\nLo siento mucho, se que es algo demaciado doloroso, ¿Quieres seguir platicando?..."
	if ev == 2:
            STATES['amigo'] = True
            ans =ans + "\nQue fuerte, lo siento ¿Quieres seguir platicando?..."

    NO_TRA = re.compile('(.*|^)((no\strabajo)|(no\stengo\strabajo))($|.*)');
    NO_MATCH = re.match(NO_TRA,message_)
    if NO_MATCH:
        my_conexion.cambiar_estado('trabajo',username)
        STATES['trabajo'] = True

    NO_ESC = re.compile('(.*|^)no\sestudio($|.*)');
    NO_MATCH = re.match(NO_ESC,message_)
    if NO_MATCH:
        my_conexion.cambiar_estado('escuela',username)
        STATES['escuela'] = True
	
    MAMA = re.compile('(.*|^)((M|m)i\s(mama|mamá|madre)\s(es|esta)(.*|algo|un poco|mucho|mucho muy|muy)\s(excelente|bien|alegre|animada|apasionada|cariñosa|contenta|encantada|euforica|exitada|feliz|satisfecha|orgullosa))($|.*)');
    MAMA_MATCH = re.match(MAMA,message_)
    if MAMA_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nOh Que bien que tu mamá este asi..."
	if ev == 2:
        	ans =ans + "\nMe alegra leer esto de tu mamá..."
	if ev == 3:
        	ans =ans + "\nMaravilloso, que todo siga asi para tu mamá..."
	STATES['mama'] = True

    MAMA = re.compile('(.*|^)((M|m)i\s(mama|mamá|madre)\s(es|esta)(.*|algo|un poco|mucho|mucho muy|muy)\s(abrumada|mal|mala|enferma|afligida|agotada|amargada|angustiada|apatica|arrepentida|asustada|aterrada|avergonzada|celosa|cansada|confundida|debil|decaida|decepcionada|deprimida|desanimada|desesperada|enojada|infeliz|herida|insegura|triste|tensa|molesta|irritada))($|.*)');
    MAMA_MATCH = re.match(MAMA,message_)
    if MAMA_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nmmm que mal que tu mama este asi..."
	if ev == 2:
        	ans =ans + "\nLo siento, que todo mejore para tu mamá..."
	if ev == 3:
        	ans =ans + "\nLeer esto de tu mama no me gusta, lo siento por ella..."
	STATES['mama'] = True

    PAPA = re.compile('(.*|^)((M|m)i\s(papa|papá|padre)\s(es|esta)(.*|algo|un poco|mucho|mucho muy|muy)\s(excelente|bien|alegre|animado|apasionado|cariñoso|contento|encantado|euforico|exitado|feliz|satisfecho|orgullos))($|.*)');
    PAPA_MATCH = re.match(PAPA,message_)
    if PAPA_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nOh Que bien que tu papá este así..."
	if ev == 2:
        	ans =ans + "\nMe alegra leer esto de tu papá..."
	if ev == 3:
        	ans =ans + "\nMaravilloso, que todo siga asi para tu padre..."
	STATES['papa'] = True

    PAPA = re.compile('(.*|^)((M|m)i\s(papa|papá|padre)\s(es|esta)(.*|algo|un poco|mucho|mucho muy|muy)\s(abrumado|mal|afligido|agotado|malo|enfermo|amargado|angustiado|apatico|arrepentido|asustado|aterrado|avergonzado|celoso|cansado|confundido|debil|decaido|decepcionado|deprimido|desanimado|desesperado|enojado|infeliz|herido|inseguro|triste|tenso|molesto|irritado))($|.*)');
    PAPA_MATCH = re.match(PAPA,message_)
    if PAPA_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nmmm que mal que tu papa este asi..."
	if ev == 2:
        	ans =ans + "\nLo siento, que todo mejore para tu papa..."
	if ev == 3:
        	ans =ans + "\nLeer esto de tu papa no me gusta, lo siento por ella..."
	STATES['papa'] = True

    HERMANO = re.compile('(.*|^)((M|m)i\s(herman(o|a))\s(es|esta)(.*|algo|un poco|mucho|mucho muy|muy)\s(excelente|bien|alegre|animado|apasionado|cariñoso|contento|encantado|euforico|exitado|feliz|satisfecho|orgullos))($|.*)');
    HERMANO_MATCH = re.match(HERMANO,message_)
    if HERMANO_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nOh Que bien que tu hermano este asi..."
	if ev == 2:
        	ans =ans + "\nMe alegra leer esto de tu hermano..."
	if ev == 3:
        	ans =ans + "\nMaravilloso, que todo siga asi para tu hermano..."
	STATES['hermano'] = True

    HERMANO = re.compile('(.*|^)((M|m)i\s(herman(o|a))\s(es|esta)(.*|algo|un poco|mucho|mucho muy|muy)\s(abrumado|afligido|agotado|malo|enfermo|amargado|angustiado|apatico|arrepentido|asustado|aterrado|avergonzado|celoso|cansado|confundido|debil|decaido|decepcionado|deprimido|desanimado|desesperado|enojado|infeliz|herido|inseguro|triste|tenso|molesto|irritado))($|.*)');
    HERMANO_MATCH = re.match(HERMANO,message_)
    if HERMANO_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nmmm que mal que tu hermano este asi..."
	if ev == 2:
        	ans =ans + "\nLo siento, que todo mejore para tu hermano..."
	if ev == 3:
        	ans =ans + "\nLeer esto de tu hermano no me gusta, lo siento por ella..."
	STATES['hermano'] = True

    MASCOTA = re.compile('(.*|^)((M|m)i(.*|s)\s(mascota|perro|gato|pajaro|pez|rana|tortuga|iguana)(.*|s)\s(es|esta|estan|son)(.*|algo|un poco|mucho|mucho muy|muy)\s(excelente(.*|s)|bien|alegre(.*|s)|animad(o|a)(.*|s)|apasionad(o|a)(.*|s)|cariños(o|a)(.*|s)|content(o|a)(.*|s)|encantad(o|a)(.*|s)|euforic(o|a)(.*|s)|exitad(o|a)(.*|s)|feliz|felices|satisfech(o|a)(.*|s)|orgullos(o|a)(.*|s)))($|.*)');
    MASCOTA_MATCH = re.match(MASCOTA,message_)
    if MASCOTA_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nOh Que bien que tu mascota este asi..."
	if ev == 2:
        	ans =ans + "\nMe alegra leer esto de tu mascota..."
	if ev == 3:
        	ans =ans + "\nMaravilloso, que todo siga asi para tu mascota..."
	STATES['mascota'] = True

    MASCOTA = re.compile('(.*|^)((M|m)i(.*|s)\s(mascota|perro|gato|pajaro|pez|rana|tortuga|iguana)(.*|s)\s(es|esta|estan|son)(.*|algo|un poco|mucho|mucho muy|muy)\s(abrumad(o|a)(.*|s)|mal(o|a)|enferm(o|a)|afligid(o|a)(.*|s)|agotad(o|a)(.*|s)|amargad(o|a)(.*|s)|angustiad(o|a)(.*|s)|apatic(o|a)(.*|s)|arrepentid(o|a)(.*|s)|asustad(o|a)(.*|s)|aterrad(o|a)(.*|s)|avergonzad(o|a)(.*|s)|celos(o|a)(.*|s)|cansad(o|a)(.*|s)|confundid(o|a)(.*|s)|debil|debiles|decaid(o|a)(.*|s)|decepcionad(o|a)(.*|s)|deprimid(o|a)(.*|s)|desanimad(o|a)(.*|s)|desesperad(o|a)(.*|s)|enojad(o|a)(.*|s)|infeliz|infelices|herid(o|a)(.*|s)|insegur(o|a)(.*|s)|triste(.*|s)|tens(o|a)(.*|s)|molest(o|a)(.*|s)|irritad(o|a)(.*|s)))($|.*)');
    MASCOTA_MATCH = re.match(MASCOTA,message_)
    if MASCOTA_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nmmm que mal que tu mascota este asi..."
	if ev == 2:
        	ans =ans + "\nLo siento, que todo mejore para tu mascota..."
	if ev == 3:
        	ans =ans + "\nLeer esto de tu mascota no me gusta, lo siento por ella..."
	STATES['mascota'] = True

    AMIGO = re.compile('(.*|^)((M|m)i(.*|s)\s(mejores amigos|mejor amigo|amig(o|a)(.*|s))\s(es|esta|son|estan)(.*|algo|un poco|mucho|mucho muy|muy)\s(excelente(.*|s)|bien|alegre|alegres|animad(o|a)|animad(o|a)s|apasionad(o|a)|apasionad(o|a)s|cariños(o|a)|cariños(o|a)s|content(o|a)|content(o|a)s|encantad(o|a)|encantad(o|a)s|euforic(o|a)|euforic(o|a)s|exitad(o|a)|exitad(o|a)s|feliz|felices|satisfech(a|o)|satisfech(o|a)s|orgullos(o|a)|orgullos(o|a)s))($|.*)');
    AMIGO_MATCH = re.match(AMIGO,message_)
    if AMIGO_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nOh Que bien que tu amigo este asi..."
	if ev == 2:
        	ans =ans + "\nMe alegra leer esto de tu amigo..."
	if ev == 3:
        	ans =ans + "\nMaravilloso, que todo siga asi para tu amigo..."
	STATES['amigo'] = True

    AMIGO = re.compile('(.*|^)((M|m)i(.*|s)\s(mejores amigos|mejor amigo|amig(o|a)(.*|s))\s(es|esta|son|estan)(.*|algo|un poco|mucho|mucho muy|muy)\s(abrumad(o|a)(.*|s)|afligid(o|a)(.*|s)|agotad(o|a)(.*|s)|amargad(o|a)(.*|s)|angustiad(o|a)(.*|s)|apatic(o|a)(.*|s)|arrepentid(o|a)(.*|s)|asustad(o|a)(.*|s)|aterrad(o|a)(.*|s)|avergonzad(o|a)(.*|s)|celos(o|a)(.*|s)|cansad(o|a)(.*|s)|confundid(o|a)(.*|s)|debil|debiles|decaid(o|a)(.*|s)|decepcionad(o|a)(.*|s)|deprimid(o|a)(.*|s)|desanimad(o|a)(.*|s)|desesperad(o|a)(.*|s)|enojad(o|a)(.*|s)|infeliz|infelices|herid(o|a)(.*|s)|insegur(o|a)(.*|s)|triste(.*|s)|tens(o|a)(.*|s)|molest(o|a)(.*|s)|irritad(o|a)(.*|s)))($|.*)');
    AMIGO_MATCH = re.match(AMIGO,message_)
    if AMIGO_MATCH:
	ev = random.randint(1, 3)
	if ev == 1:
        	ans =ans + "\nmmm que mal que tu amigo este asi..."
	if ev == 2:
        	ans =ans + "\nLo siento, que todo mejore para tu amigo..."
	if ev == 3:
        	ans =ans + "\nLeer esto de tu amigo no me gusta, lo siento por ella..."
	STATES['amigo'] = True

    TRABAJO = re.compile('(.*|^)(((M|m)i|(E|e)l|(E|e)n\sel)\s(negocio|empleo|trabajo)\s(es|esta|son|estuvo))($|.*)');
    TRABAJO_MATCH = re.match(TRABAJO,message_)
    if TRABAJO_MATCH:
	STATES['trabajo'] = True

    ESCUELA = re.compile('(.*|^)(((M|m)i|(E|e)l|(E|e)n\sel)\s(escuela|universidad|prepa|preparatoria|secu|secundaria|primaria)\s(es|esta|son|estuvo))($|.*)');
    ESCUELA_MATCH = re.match(ESCUELA,message_)
    if ESCUELA_MATCH:
	STATES['escuela'] = True

#Conversaciones del Bot

    if vez > 0:
        ev = random.randint(1, 9)
        if ev == 1:
            ans = ans + "\n ¿cómo te fue hoy?..."
        if ev == 2:
            ans = ans + "\n ¿cómo estuvo tu dia de hoy?..."
        if ev == 3:
            ans = ans + "\n ¿que hiciste el dia de hoy?..."
        if ev == 4:
            ans = ans + "\n ¿algo interesante que hicieras hoy?..."
        if ev == 5:
            ans = ans + "\n ¿que te paso el dia de hoy?..."
        if ev == 6:
            ans = ans + "\n ¿Que mas hiciste en tu dia?..."
        if ev == 7:
            ans = ans + "\n Y ¿Que mas?..."
        if ev == 8:
            ans = ans + "\n ¿Algo mas que quieras platicarme?..."
        if ev == 9:
            ans = ans + "\n ¿Que mas hiciste?..."

    if vez == 0:
        ev = random.randint(1, 4)
        if ev == 1:
            ans = ans + "\n ¿cómo estas hoy?..."
        if ev == 2:
            ans = ans + "\n ¿cómo te sientes el dia de hoy?..."
        if ev == 3:
            ans = ans + "\n ¿cómo te sentiste hoy?..."
        if ev == 4:
            ans = ans + "\n ¿que te paso el dia de hoy?..."
	
    # REVISAR ESTADO
    if STATES[username]['mama']== 'False':
        print(vez)
        if vez > 2:
            ans=ans + "\n Cuéntame, ¿Como esta tu mamá?"
    elif STATES['papa']== 'False':
        if vez > 0:
            ans=ans + "\n¿Cómo esta tu papá?"
    elif STATES['hermano']== 'False':
        if vez > 0:
            ans=ans + "\n¿Que tal tu hermano?"
    elif STATES['mascota']== 'False':
        if vez > 0:
            ans=ans + "\n¿Que tal tu mascota?"
    elif STATES['amigo']== 'False':
        if vez > 0:
            ans=ans + "\n¿Como esta tu mejor amigo?"
    elif STATES['escuela']== 'False':
        if vez > 0:
            ans=ans + "\n¿Como vas en la escuela?"
    elif STATES['trabajo']== 'False':
        if vez > 0:
            ans=ans + "\n¿Como estubo el trabajo?"




    ADIOS = re.compile('(H|h)asta\sluego|HASTA\sLUEGO|(A|a)di(o|ó)s|ADI(O|Ó)S|(N|n)os\svemos|NOS\sVEMOS|(C|c)hao|CHAO|(B|b)ye|BYE($)');
    ADIOS_MATCH = re.match(ADIOS,message_)
    if ADIOS_MATCH:
        vez = 100
	ev = random.randint(1, 4)
	if ev == 1:
        	ans ="\n Adios, fue un gusto platicar contigo."
	if ev == 2:
        	ans ="\n Adios, Me encanta platicar contigo."
    if ev == 3:
        	ans ="\n Adios, Te deseo suerte y que tus dias sean mejores."
    if ev == 4:
        	ans ="\n Adios, Espero que vuelvas a platicar conmigo.... ;)"

       
    vez = vez + 1
    STATES['vez'] = vez
        
    return ans

def sinAcentos(Mensaje):
    cadena= ''.join((c for c in unicodedata.normalize('NFD',unicode(Mensaje)) if unicodedata.category(c) != 'Mn'))
    return cadena.decode().lower()
