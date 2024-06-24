#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-info">
# Привет, Артем! Меня зовут Светлана Чих и я буду проверять твой проект. Моя основная цель — не указать на совершенные тобою ошибки, а поделиться своим опытом и помочь тебе. Предлагаю общаться на «ты». Но если это не удобно - дай знать, и мы перейдем на «вы».
# 
# <div class="alert alert-success">
# <b>👍 Успех:</b> Зелёным цветом отмечены удачные и элегантные решения, на которые можно опираться в будущих проектах.
# </div>
# <div class="alert alert-warning">
# <b>🤔 Рекомендация:</b> Жёлтым цветом выделено то, что в следующий раз можно сделать по-другому. Ты можешь учесть эти комментарии при выполнении будущих заданий или доработать проект сейчас (однако это не обязательно).
# </div>
# <div class="alert alert-danger">
# <b>😔 Необходимо исправить:</b> Красным цветом выделены комментарии, без исправления которых, я не смогу принять проект :(
# </div>
# <div class="alert alert-info">
# <b>👂 Совет:</b> Какие-то дополнительные материалы
# </div>
# Давай работать над проектом в диалоге: если ты что-то меняешь в проекте по моим рекомендациям — пиши об этом.
# Мне будет легче отследить изменения, если ты выделишь свои комментарии:
# <div class="alert alert-info"> <b>🎓 Комментарий студента:</b> Например, вот так.</div>
# Пожалуйста, не перемещай, не изменяй и не удаляй мои комментарии. Всё это поможет выполнить повторную проверку твоего проекта быстрее.
#  </div>
# 

# # Проект: телекоммуникации

# <div class="alert">
# <h2> Описание проекта <a class="tocSkip"> </h2>
# 
# Оператор связи «ТелеДом» хочет бороться с оттоком клиентов. Для этого его сотрудники начнут предлагать промокоды и специальные условия всем, кто планирует отказаться от услуг связи. Чтобы заранее находить таких пользователей, «ТелеДому» нужна модель, которая будет предсказывать, разорвёт ли абонент договор. Команда оператора собрала персональные данные о некоторых клиентах, информацию об их тарифах и услугах. Моя задача — обучить на этих данных модель для прогноза оттока клиентов.
# 
# Оператор предоставляет два основных типа услуг: 
# Стационарную телефонную связь. Телефон можно подключить к нескольким линиям одновременно.
# Интернет. Подключение может быть двух типов: через телефонную линию (DSL, от англ. digital subscriber line — «цифровая абонентская линия») или оптоволоконный кабель (Fiber optic).
# 
# Также доступны такие услуги:
# Интернет-безопасность: антивирус (DeviceProtection) и блокировка небезопасных сайтов (OnlineSecurity);
# Выделенная линия технической поддержки (TechSupport);
# Облачное хранилище файлов для резервного копирования данных (OnlineBackup);
# Стриминговое телевидение (StreamingTV) и каталог фильмов (StreamingMovies).
# Клиенты могут платить за услуги каждый месяц или заключить договор на 1–2 года. Возможно оплатить счёт разными способами, а также получить электронный чек.
# 
# <b> Описание данных </b> 
# 
# Данные состоят из нескольких файлов, полученных из разных источников: \
# contract_new.csv — информация о договоре; \
# personal_new.csv — персональные данные клиента; \
# internet_new.csv — информация об интернет-услугах; \
# phone_new.csv — информация об услугах телефонии. 
# 
# 
# <b> Файл contract_new.csv </b> \
# customerID — идентификатор абонента; \
# BeginDate — дата начала действия договора; \
# EndDate — дата окончания действия договора; \
# Type — тип оплаты: раз в год-два или ежемесячно; \
# PaperlessBilling — электронный расчётный лист; \
# PaymentMethod — тип платежа; \
# MonthlyCharges — расходы за месяц; \
# TotalCharges — общие расходы абонента. 
#     
# <b> Файл personal_new.csv </b> \
# customerID — идентификатор пользователя; \
# gender — пол; \
# SeniorCitizen — является ли абонент пенсионером; \
# Partner — есть ли у абонента супруг или супруга; \
# Dependents — есть ли у абонента дети.
# 
# <b> Файл internet_new.csv </b> \
# customerID — идентификатор пользователя; \ 
# InternetService — тип подключения; \
# OnlineSecurity — блокировка опасных сайтов; \
# OnlineBackup — облачное хранилище файлов для резервного копирования данных; \
# DeviceProtection — антивирус; \
# TechSupport — выделенная линия технической поддержки; \
# StreamingTV — стриминговое телевидение; \
# StreamingMovies — каталог фильмов.
# 
# <b> Файл phone_new.csv </b> \
# customerID — идентификатор пользователя; \
# MultipleLines — подключение телефона к нескольким линиям одновременно. 
#     
# Во всех файлах столбец customerID содержит код клиента. Информация о договорах актуальна на 1 февраля 2020 года.

# In[1]:


get_ipython().system('pip install phik')


# In[2]:


# импорт библиотек

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import phik
from phik import resources, report

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score 
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from catboost import CatBoostClassifier
from sklearn.metrics import roc_curve, auc, confusion_matrix, roc_auc_score

import warnings
warnings.filterwarnings("ignore")


# In[3]:


RANDOM_STATE = 190224
scaler = StandardScaler()
encoder = OneHotEncoder(sparse=False, drop='first') 


# <div class="alert alert-success">
# <b>👍 Успех:</b> Импортированы нужные библиотеки, определены константы!
# </div>

# In[4]:


# инициализация входных данных

contract = pd.read_csv('/datasets/contract_new.csv', parse_dates={"date": ["BeginDate"]})
personal = pd.read_csv('/datasets/personal_new.csv')
internet = pd.read_csv('/datasets/internet_new.csv')
phone = pd.read_csv('/datasets/phone_new.csv')


# ### Общая информация

# In[5]:


def general_info(data):
    display(data.head(10))
    print('-------------------------------INFO-----------------------------------')
    display(data.info())
    print('-------------------------------DESCRIBE-------------------------------')
    display(data.describe(percentiles=[0.05, 1/4, 1/2, 3/4, 0.95]).T)


# #### Датасет contract

# In[6]:


general_info(contract)


# In[7]:


print(f"Пропущенные значения в contract:")
pd.DataFrame(round(contract.isna().mean()*100,1)).style.background_gradient('coolwarm')


# <b>Первые заметки по датасету contract: </b>
# * Необходимо привести все наименования столбцов согласно PEP8.
# * Верно указать формат данных (BeginDate к формату даты, EndDate - проверить, скорей всего тоже дата, TotalCharges - float64).

# In[8]:


# Наименование PEP 8
contract = contract.rename(columns={'customerID': 'CustomerID', 'date': 'BeginDate'})
contract.head(1)


# In[9]:


# Певередем totalcharges в формат float
contract.TotalCharges = pd.to_numeric(contract.TotalCharges, errors ='coerce')
contract.info()


# In[10]:


print(f"Пропущенные значения в contract:")
pd.DataFrame(round(contract.isna().mean()*100,1)).style.background_gradient('coolwarm')


# В столбце totalcharges появились пустые значения, давайте их проверим.

# In[11]:


contract.loc[contract.TotalCharges.isna()==True]


# Всего 11 позиций, если судить логически то это клиенты которые только что заключили договор с оплатой раз в один/два года, предлагаю заполнить их расходы значением 0

# <div class="alert alert-success">
# <b>👍 Успех:</b> Все верно! Деньги от них еще не поступили
# </div>

# In[12]:


contract.TotalCharges = contract.TotalCharges.fillna(0)


# In[13]:


print(f"Пропущенные значения в contract:")
pd.DataFrame(round(contract.isna().mean()*100,1)).style.background_gradient('coolwarm')


# In[14]:


contract.query("CustomerID=='4472-LVYGI'")


# <div class="alert alert-success">
# <b>👍 Успех:</b> Все верно!
# </div>

# #### Датасет personal

# In[15]:


general_info(personal)


# In[16]:


print(f"Пропущенные значения в personal:")
pd.DataFrame(round(personal.isna().mean()*100,1)).style.background_gradient('coolwarm')


# <b>Первые заметки по датасету personal: </b>
# * Необходимо привести все наименования столбцов согласно PEP8.

# In[17]:


# Наименование PEP 8
personal = personal.rename(columns={'customerID': 'CustomerID', 'gender': 'Gender'})
personal.head(1)


# <div class="alert alert-success">
# <b>👍 Успех:</b> Все верно!
# </div>

# #### Датасет internet

# In[18]:


general_info(internet)


# In[19]:


print(f"Пропущенные значения в internet:")
pd.DataFrame(round(internet.isna().mean()*100,1)).style.background_gradient('coolwarm')


# <b>Первые заметки по датасету internet: </b>
# * Необходимо привести все наименования столбцов согласно PEP8.

# In[20]:


# Наименование PEP 8
internet = internet.rename(columns={'customerID': 'CustomerID'})
internet.head(1)


# <div class="alert alert-success">
# <b>👍 Успех:</b> Все верно!
# </div>

# #### Датасет phone

# In[21]:


general_info(phone)


# In[22]:


print(f"Пропущенные значения в phone:")
pd.DataFrame(round(phone.isna().mean()*100,1)).style.background_gradient('coolwarm')


# <b>Первые заметки по датасету phone: </b>
# * Необходимо привести все наименования столбцов согласно PEP8.

# In[23]:


# Наименование PEP 8
phone = phone.rename(columns={'customerID': 'CustomerID'})
phone.head(1)


# #### Общие выводы по первому пункту работы:
# * на входе имеем четыре датасета, их описание указано в начале проекта;
# * проверили датасеты на пропуски;
# * заполнили пропуски в столбце TotalCharges (новые клиенты);
# * привели наименование столбцов в каждом датасете к PEP 8;
# * привели данные к верному типу данных.

# <div class="alert alert-success">
# <b>👍 Успех:</b> Датасеты загружены, просмотрены и обработаны!
# </div>

# ### Исследовательский анализ и предобработка данных

# In[24]:


# Функция временных переменных для создания графиков

def count_all (data, col):
    y = data.groupby(col)[col].count().sort_values(ascending=False)
    return y


# In[25]:


display(f'Дубликаты contract: {contract.duplicated().sum()}')
display(f'Дубликаты personal: {personal.duplicated().sum()}')
display(f'Дубликаты internet: {internet.duplicated().sum()}')
display(f'Дубликаты phone: {phone.duplicated().sum()}')


# Дубликатов во всех датасетах нет

# <div class="alert alert-success">
# <b>👍 Успех:</b> Все верно!
# </div>

# #### Датасет contract

# In[26]:


contract.nunique()


# In[27]:


contract.head(3)


# Предлагаю создать новый столбец - Sign , в котором зададим целевой признак 0 - клиент остался, 1 - клиент ушел, сгенерируем данные из столбца EndDate. В столбце EndDate 'No' заполним крайней датой (2020-02-01), чтобы можно посчитать общее время пользованием услугами связи и создадим для этого новый признак - UseTime

# In[28]:


contract['Sign'] = (contract['EndDate'] != 'No').astype(int)
contract.sample(5)


# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Отнекиваться не буду, код подглядел. Сам не смог разобраться как заменить все позиции с датами на 1, нужно либо через цикл прогонять, либо кортеж создавать? Вообщем итак и так не получилось. Да и почему в данном коде создаётся 0 и 1 тоже не могу понять...
# </div>

# <div class="alert alert-warning">
# <b>🤔 Рекомендация:</b> Здесь проверяется условкие и в итоге получается булево знвчение - False или True при приобразовании в целое цисло получают 0 и 1
# </div>

# In[29]:


contract['EndDate'] = contract['EndDate'].replace({'No': '2020-02-01'})


# In[30]:


contract['EndDate'].nunique()


# In[31]:


# приведем тип данных EndDate к типу данных
contract['EndDate'] = pd.to_datetime(contract['EndDate'], format='%Y-%m-%d')


# In[32]:


contract.head(7)


# In[33]:


# новый столбец с количеством дней пользования услугами связи
contract['UseTime'] = (contract['EndDate'] - contract['BeginDate']).dt.days


# In[34]:


contract.head()


# <div class="alert alert-success">
# <b>👍 Успех:</b> Создан новый признак! Он пригодится в обучении модели
# </div>

# In[35]:


contract.info()


# In[36]:


# временные переменные для создания графиков
Type_count, PaperlessBilling_count, PaymentMethod_count, Sign_count = (
                                                                       count_all(contract, 'Type'),
                                                                       count_all(contract, 'PaperlessBilling'),
                                                                       count_all(contract, 'PaymentMethod'),
                                                                       count_all(contract, 'Sign')
                                                                       )


# In[37]:


plt.figure(figsize=(20, 10))
plt.subplot(1, 4, 1)
Type_count.plot(kind = 'pie', title = 'Распределение Type', autopct = '%1.0f%%')
plt.subplot(1, 4, 2)
PaperlessBilling_count.plot(kind = 'pie', title = 'Распределение PaperlessBilling', autopct = '%1.0f%%', labels=['Да', 'Нет'])
plt.subplot(1, 4, 3)
PaymentMethod_count.plot(kind = 'pie', title = 'Распределение PaymentMethod', autopct = '%1.0f%%')
plt.subplot(1, 4, 4)
Sign_count.plot(kind = 'pie', title = 'Распределение Sign', autopct = '%1.0f%%', labels=['Нет', 'Да']);


# In[38]:


contract.MonthlyCharges.hist(bins='auto', figsize=(15,5))
plt.title('Гистограмма расходов за месяц (MonthlyCharges)', size=15)
plt.xlabel('Сумма')
plt.ylabel('Количество')
plt.show();


# In[39]:


contract.UseTime.hist(bins='auto', figsize=(15,5))
plt.title('Гистограмма пользования услугами связи (UseTime)', size=15)
plt.xlabel('Сумма в днях')
plt.ylabel('Количество клиентов')
plt.show();


# In[40]:


contract.TotalCharges.hist(bins='auto', figsize=(15,5))
plt.title('Гистограмма общих расходов абонента (TotalCharges)', size=15)
plt.xlabel('Сумма')
plt.ylabel('Количество клиентов')
plt.show();


# In[41]:


contract.query('TotalCharges < 1000 ')


# In[42]:


aaa = 2965/7043*100
aaa


# In[43]:


# переменная для phik
contract_phik = contract.drop('CustomerID', axis=1)


# In[44]:


contract_phik.phik_matrix(interval_cols=['MonthlyCharges', 'TotalCharges', 'Sign', 'UseTime'])


# Общие выводы:
# * создан целевой признак Sign, где 0 человек продолжает пользоваться услугами, 1 - человек прекратил пользоваться услугами;
# * создан новый признак UseTime показывающий сколько человек является/являлись абонентом;
# * cтолбец BeginData приведен к типу даты, наименования No заменены на дату выгрузки датасетов (2020-02-01);
# * распределение по признаку Type (тип оплаты: раз в год-два или ежемесячно): 55% оплачивают услуги кажды месяц, 24% раз в два года, 21% раз в год;
# * распределение по признаку PaperlessBilling (электронный расчётный лист): 59% абонентов пользуются, 41% нет;
# * распределение по признаку PaymentMethod (тип платежа): 31% используют электронный чек, 23% paymentMethod(любые платежные средства), 22% у Bank transfer и credit card;
# * распределение Sign (перестал пользоваться услугами связи (целевой признак)) 84% продолжают, 16% прекратили;
# * гистограмма расходов за месяц (MonthlyCharges) подтвердила, что большинство клиентов оплачивают услуги раз в месяц;
# * гистограмма пользования услугами связи (UseTime) показала, что клиенты либо пользуются услугами меньше года и уходят, либо пользуются услугами больше 2000 дней;
# * большинство клиентов принесло доход до 1000 у.е., что составляет 42%
# * большая корреляционная связь у UseTime к BeginDate (97%), UseTime к TotalCharges (84%), TotalCharges к BeginDate (77%), TotalCharges к MonthlyCharges (71%); 
# * пропуски не обнаружены.

# <div class="alert alert-success">
# <b>👍 Успех:</b> Все верно! Датасет исследован
# </div>

# #### Датасет personal

# In[45]:


personal.head(3)


# In[46]:


#В данном датасете бинарные данные, предлагаю сразу перевести их в 1 или 0, чтобы в дальнейшем кодировщик не создавал новые столбцы
#personal['Gender'] = personal['Gender'].replace({'Female': '0', 'Male': '1'})
#personal['Partner'] = personal['Partner'].replace({'No': '0', 'Yes': '1'})
#personal['Dependents'] = personal['Dependents'].replace({'No': '0', 'Yes': '1'})


# In[47]:


personal.nunique()


# In[48]:


# временные переменные для создания графиков
Gender_count, SeniorCitizen_count, Partner_count,  Dependents_count = (
                                                                       count_all(personal, 'Gender'), 
                                                                       count_all(personal, 'SeniorCitizen'), 
                                                                       count_all(personal, 'Partner'), 
                                                                       count_all(personal, 'Dependents')
                                                                      ) 


# In[49]:


plt.figure(figsize=(20, 10))
plt.subplot(1, 4, 1)
Gender_count.plot(kind = 'pie', title = 'Распределение Gender', autopct = '%1.0f%%', labels=['Мужчина', 'Женщина'])
plt.subplot(1, 4, 2)
SeniorCitizen_count.plot(kind = 'pie', title = 'Распределение SeniorCitizen', autopct = '%1.0f%%', labels=['Не пенсионер', 'Пенсионер'])
plt.subplot(1, 4, 3)
Partner_count.plot(kind = 'pie', title = 'Распределение Partner', autopct = '%1.0f%%', labels=['Холост', 'Женат'])
plt.subplot(1, 4, 4)
Dependents_count.plot(kind = 'pie', title = 'Распределение Dependents', autopct = '%1.0f%%', labels=['Нет детей', 'Есть дети']);


# In[50]:


personal.iloc[:,1:].phik_matrix(interval_cols=['SeniorCitizen'])


# Выводы по personal:
# * Мужчин и женщин поровну;
# * Пенсионеров 16% от общей массы;
# * Замужних/женатых людей примерно поровну по отношению к незамужним/неженатым;
# * Дети есть у 30% абонентов;
# * Сильная корреляционная связь у Gender и Dependents, хорошая связь у Dependents и Partner (65%).

# <div class="alert alert-success">
# <b>👍 Успех:</b> Все верно!
# </div>

# #### Датасет internet

# In[51]:


internet.head(3)


# In[52]:


internet.nunique()


# По аналогии с датасетом personal предлагаю сразу заменить на 1 и 0

# In[53]:


# временные переменные для создания графиков
(
    OnlineSecurity_count, 
    OnlineBackup_count, 
    DeviceProtection_count, 
    TechSupport_count, 
    StreamingTV_count, 
    StreamingMovies_count
) = (
    count_all(internet, 'OnlineSecurity'), 
    count_all(internet, 'OnlineBackup'), 
    count_all(internet, 'DeviceProtection'), 
    count_all(internet, 'TechSupport'), 
    count_all(internet, 'StreamingTV'), 
    count_all(internet, 'StreamingMovies')
    ) 


# In[54]:


plt.figure(figsize=(20, 10))
plt.subplot(1, 3, 1)
OnlineSecurity_count.plot(kind = 'pie', title = 'Распределение OnlineSecurity', autopct = '%1.0f%%', labels=['Нет', 'Да'])
plt.subplot(1, 3, 2)
OnlineBackup_count.plot(kind = 'pie', title = 'Распределение OnlineBackup', autopct = '%1.0f%%', labels=['Нет', 'Да'])
plt.subplot(1, 3, 3)
DeviceProtection_count.plot(kind = 'pie', title = 'Распределение DeviceProtection', autopct = '%1.0f%%', labels=['Нет', 'Да']);


# In[55]:


plt.figure(figsize=(20, 10))
plt.subplot(1, 3, 1)
TechSupport_count.plot(kind = 'pie', title = 'Распределение TechSupport', autopct = '%1.0f%%', labels=['Нет', 'Да'])
plt.subplot(1, 3, 2)
StreamingTV_count.plot(kind = 'pie', title = 'Распределение StreamingTV', autopct = '%1.0f%%', labels=['Нет', 'Да'])
plt.subplot(1, 3, 3)
StreamingMovies_count.plot(kind = 'pie', title = 'Распределение StreamingMovies', autopct = '%1.0f%%', labels=['Нет', 'Да']);


# In[56]:


internet.iloc[:,1:].phik_matrix()#interval_cols=[''])


# Выводы:
# * Хорошая корреляционная связь между StreamingMovies и StreamingTV (63%);
# * Распределение по данным каждого столбца указаны на графиках, подробно расписывать не вижу смысла, особо ничего не выделяется, всё примерно пополам.

# <div class="alert alert-success">
# <b>👍 Успех:</b> Все верно!
# </div>

# #### Датасет phone

# In[57]:


phone.head(3)


# In[58]:


phone.nunique()


# In[59]:


# временные переменные для создания графиков
MultipleLines_count = count_all(phone, 'MultipleLines')


# In[60]:


plt.figure(figsize=(10, 5))
MultipleLines_count.plot(kind = 'pie', title = 'Распределение MultipleLines', autopct = '%1.0f%%', labels=['Нет', 'Да']);


# Выводы:
# * распределение примерно 53% на 47%.

# <div class="alert alert-success">
# <b>👍 Успех:</b> Все верно!
# </div>

# ### Объединение данных

# Объединим все 4 датасета в один для дальнейшей работы, более информативным и важным считаю датасет contract, поэтому предлагаю к нему присоединять остальные датасеты по очереди, за ключевое поле возьмем столбец CustomerID

# In[61]:


data = contract.merge(personal, how='left', on='CustomerID')
data = data.merge(internet, how='left', on='CustomerID')
data = data.merge(phone, how='left', on='CustomerID')


# <div class="alert alert-success">
# <b>👍 Успех:</b> Все верно! Выбран правильный тип и порядок объединения
# </div>

# In[62]:


general_info(data)


# Видны пропуски по нескольким столбцам, скорей всего это случилось из-за того, что не все пользователи используют все услуги.

# In[63]:


data.isnull().sum()


# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Меня смущает, что везде одинаковое количество пропусков - 1526
# </div>

# <div class="alert alert-warning">
# <b>🤔 Рекомендация:</b> Да, это так, а почему такое могло случится? В каком датасете были эти признаки? Совпадали размеры датасетов? Что произошло при левом объединении? Без понимания природы признаков не получится корректно их заполнить
# </div>

# <div class="alert alert-info">
# <h2> Комментарий студента v2<a class="tocSkip"> </h2>
# 
# Я понял, в двух датасетах меньше записей, совсем вылетело из головы, благодарю.
# </div>

# <div class="alert alert-success">
# <b>👍 Успех:</b> Все верно))) Может нужно немного отдыхать? У тебя все хорошо получается
#     
# </div>

# In[64]:


bool_series = pd.isnull(data["DeviceProtection"])
data[bool_series]


# Если люди не пользуются услугами, предлагаю заменить пустые значения на No

# <div class="alert alert-warning">
# <b>🤔 Рекомендация:</b> Значение No используется если не подключена конкретная услуга, но подключен интерент или телефон. Заполнение всех пропусков этим значением не даст различий между этими данными
# </div>

# In[65]:


data = data.fillna('No')


# In[66]:


data.isnull().sum()


# пустых значений больше нет

# <div class="alert alert-success">
# <b>👍 Успех:</b> Все верно!
# </div>

# ### Исследовательский анализ и предобработка данных объединённого датафрейма

# In[67]:


data.head(3)


# Предлагаю более подробно рассмотреть отток клиентов.

# In[68]:


sign_counts = data.groupby('Sign')['UseTime'].sum()
sign_counts.plot(kind='pie', title = 'Распределение UseTime по отношению к Sign', autopct = '%1.0f%%');


# In[69]:


data_corr = data.drop(['CustomerID'], axis=1)


# In[70]:


for column in data_corr.columns:
    data_corr.groupby('Sign')[column].hist()
    plt.title(column)
    plt.legend(['Оставшиеся', 'Отток'])
    plt.show()


# Выводы:
# * со временем люди начинают меньше отказываться от услуг связи, особенно начиная с 2017 года;
# * Отток клиентов не особо зависит от типа оплаты, уходят примерно одинаково;
# * Клиенты с электронным расчетным листом чаще отказываются от услуг;
# * Чаще всего уходят люди с типом платежа электронный чек;
# * TotalCharges показывает, что в основном уходят клиенты, которые только начали пользоваться услугами связи;
# * Целевой признак разделен 1 к 6;
# * Время пользования услугами показывает, что в среднем уходят до 1500 дней;
# * Мужчины и женщины одинакого уходят, разницы особо нет;
# * Пенсионеров в пять раз меньше и общее количество тех кто ушел также намного меньше;
# * Чаще уходят люди состоящие в браке;
# * Чаще уходят люди без детей;
# * Клиентов с подключение DSL и оптоволокно примерно одинаково, но чаще уходят люди со вторым типом подключения;
# * Все дополнительные опции показывают одинаковое распределение по оттоку клиентов, особо не влияют.

# In[71]:


plt.figure(figsize=(20,15))
sns.heatmap(data = data_corr.phik_matrix(interval_cols=['MonthlyCharges', 'TotalCharges', 'Sign', 'UseTime', 'SeniorCitizen']), annot=True)
plt.title('Матрица корреляций')
plt.show()


# Обнаружены мультиколлинеарные признаки целевого признака - EndDate, низкую корреляцию имеют следующие фичи: PaperlessBilling (0,083), Type (0.094), Gender (0.0086), SeniorSitizen (0.086). Так же сильную корреляционную связь имеют следующие столбцы UseTime и BeginDate. \
# От данных признаков лучше всего избавиться, потому что они имеют сильную линейную зависимость и могут плохо повлиять на обучение модели, предлагаю проверить отдельно на наших моделях ниже.
# 

# <div class="alert alert-danger">
# <s><b>😔 Необходимо исправить:</b> Здесь долен быть более подробный вывод, что увидели на графиках выше? На тепловой карте? Какие признаки мультиколлениарны и что с этим делать?</s>
# </div>

# <div class="alert alert-info">
# <h2> Комментарий студента v2<a class="tocSkip"> </h2>
# 
# Поправил. А так же добавил пункт 9 с доп. исследованием.
# </div>

# <div class="alert alert-success">
# <b>👍 Успех:</b> Отлично получилось!
# </div>

# ### Подготовка данных

# In[72]:


def standard_scaler(X_train, X_test, num_col_names, scaler):
    X_train_scaled = scaler.fit_transform(X_train[num_col_names])
    X_test_scaled = scaler.transform(X_test[num_col_names])
    
    X_train_scaled = pd.DataFrame(X_train_scaled, columns=num_col_names)
    X_test_scaled = pd.DataFrame(X_test_scaled, columns=num_col_names)

    return X_train_scaled, X_test_scaled


# In[73]:


def normal_encoder(X_train, X_test, encoder):
    X_train_ohe = encoder.fit_transform(X_train)
    X_test_ohe = encoder.transform(X_test)

    encoder_col_names = encoder.get_feature_names()

    X_train_ohe = pd.DataFrame(X_train_ohe, columns=encoder_col_names)
    X_test_ohe = pd.DataFrame(X_test_ohe, columns=encoder_col_names)
    return X_train_ohe, X_test_ohe


# In[74]:


data.info()


# Удаляем столбцы с датой и CustomerID, они негативно повлияют на обучение моделей

# In[75]:


df = data.drop(['BeginDate', 'EndDate', 'CustomerID'], axis=1)


# <div class="alert alert-success">
# <b>👍 Успех:</b> Все верно!
# </div>

# In[76]:


df.head(1)


# In[77]:


num_col_names = ['MonthlyCharges', 'TotalCharges', 'UseTime']
encoder_col_names = ['Type', 'PaperlessBilling', 'PaymentMethod',
                     'InternetService', 'OnlineSecurity',
                     'OnlineBackup', 'DeviceProtection',
                     'TechSupport', 'StreamingTV', 'StreamingMovies',
                     'MultipleLines', 'Gender', 'SeniorCitizen', 'Partner', 'Dependents']


# In[78]:


X = df.drop(['Sign'], axis=1)
y = df['Sign']


# In[79]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=RANDOM_STATE)


# In[80]:


display(X_train.shape)
display(X_test.shape)
display(y_train.shape)
display(y_test.shape)


# In[81]:


X_train_ohe, X_test_ohe = normal_encoder(X_train[encoder_col_names], X_test[encoder_col_names], encoder)


# In[82]:


#X_train_ohe = pd.get_dummies(X_train, drop_first=True)
#X_test_ohe = pd.get_dummies(X_test, drop_first=True)


# In[83]:


X_train_scaled, X_test_scaled = standard_scaler(X_train, X_test, num_col_names, scaler) 


# In[84]:


X_train = pd.concat([X_train_ohe, X_train_scaled], axis=1).reset_index(drop=True)
X_test = pd.concat([X_test_ohe, X_test_scaled], axis=1).reset_index(drop=True)


# In[85]:


display(X_train.shape)
display(X_test.shape)
display(y_train.shape)
display(y_test.shape)


# In[86]:


X_train.head(3)


# <div class="alert alert-success">
# <b>👍 Успех:</b> Все верно! Молодец, что проверяешь данные после кодирования и масштабирования
# </div>

# ### Обучение моделей машинного обучения

# #### Модель LogisticRegression

# In[87]:


get_ipython().run_cell_magic('time', '', "param_grid = {'C': [0.01, 0.1, 1, 10, 100]}\n\nmodel_lr = LogisticRegression(n_jobs=-1, random_state=RANDOM_STATE)\n\nsearch_lr = GridSearchCV(model_lr, param_grid, cv=3, scoring='roc_auc', verbose = False)\nsearch_lr.fit(X_train, y_train)\n\nprint('Лучшие параметры:', search_lr.best_params_)\nprint('Лучший результат:', search_lr.best_score_)")


# In[88]:


predict_lr = search_lr.best_estimator_.predict_proba(X_train)[:, 1]


# In[89]:


fpr, tpr, thresholds = roc_curve(y_train, predict_lr)  
plt.plot(fpr, tpr)     
plt.title("График зависимости FPR от TPR")
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.show()


# Метрика ROC-AUC на тренировочной выборке составила 0.77

# #### Модель CatBoostClassifier

# In[90]:


model_cb = CatBoostClassifier(random_state = RANDOM_STATE)


# In[91]:


param_cb = {'depth':[5,10], 'learning_rate':np.arange(0.1,1,0.2)}


# In[92]:


grid_cb = GridSearchCV(estimator=model_cb, param_grid=param_cb, cv=3, scoring='roc_auc')


# In[93]:


get_ipython().run_cell_magic('time', '', 'grid_cb.fit(X_train, y_train)')


# In[94]:


pred_cb = grid_cb.best_estimator_.predict(X_train)


# In[95]:


print('Лучший результат:', grid_cb.best_score_)


# ### Выбор лучшей модели

# Лучшую метрику показала модель CatBoostClassifier, проверим на тестовой выборке

# <div class="alert alert-success">
# <b>👍 Успех:</b> Лучшая модель выбрана!
# </div>

# In[96]:


predict_cb = grid_cb.best_estimator_.predict_proba(X_test)[:, 1]


# In[97]:


print(f'Метрика ROC-AUC на тестовой выборке: {round(roc_auc_score(y_test, predict_cb),3)}')


# In[98]:


fpr, tpr, thresholds = roc_curve(y_test, predict_cb)   
plt.plot(fpr, tpr)     
plt.title("График зависимости FPR от TPR")
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.show()


# In[99]:


main_sign = pd.DataFrame(grid_cb.best_estimator_.feature_importances_, index = X_test.columns, columns=['MainSign'])
main_sign = main_sign.sort_values(by='MainSign', ascending=False)
main_sign.iloc[:10]


# Самые важные признаки влияющие на результат - UseTime, TotalCharges, MonthlyCharges.

# <div class="alert alert-success">
# <b>👍 Успех:</b> Все верно!
# </div>

# In[100]:


y_pred = grid_cb.best_estimator_.predict(X_test)


# In[101]:


cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize = (5,5))
plt.title("Матрица ошибок")
ax = sns.heatmap(cm, annot=True, fmt='d', cmap='Blues_r')
plt.xlabel('Predicted label')
plt.ylabel('True label');


# истинно положительный (TP) - 1471 \
# истинно отрицательный (TN) - 164 \
# ложноположительный результат (FP), ошибка I рода - 21 \
# ложноотрицательный результат (FN), ошибка II рода 105 

# <div class="alert alert-success">
# <b>👍 Успех:</b> Все верно!
# </div>

# ### Общий вывод и рекомендации заказчику

# В данном проекте мы разработали модель по предсказанию перестанет ли клиент пользоваться услугами связи сотовой связи или нет. На входе получили 4 датасета с общий ключевым полем customerID. Далее проделали следующую работу: 
# * Провели предобработку данных: привели наименования к стандарту PEP 8, заполнили пропуски, проверили дубликаты, изменили типы данных. Провели исследователький анализ, обозначили общие выводы. 
# * Добавили новый столбец UseTime  с общим временем пользования услугами связи, увидили что он имеет хорошую корреляцию с целевым признаком и является хорошим признаком для обучения моделей.  
# * Объединили все датасеты в общий, заполнили пропущенные значения на 0. 
# * Подготовили данные для обучения моделей, удалили лишние признаки. 
# * Обучили две модели с подбором гипперпараметров - линейную классификацию и CatBoostClassifier.
# * Лучший результат показала модель CatBoostClassifier со значением метрики ROC-AUC в 90%

# <div class="alert alert-success">
# <b>👍 Успех:</b> Все верно!
# </div>

# ### Дополнительная проверка на важных признаках

# In[102]:


col_main = ['UseTime', 'TotalCharges', 'MonthlyCharges', 'x0_Two year', 'x13_Yes', 'x0_One year', 'x5_Yes', 'x10_Yes', 'x1_Yes', 'x14_Yes']


# In[103]:


search_lr.fit(X_train[col_main], y_train)


# In[104]:


print('Лучшие параметры:', search_lr.best_params_)
print('Лучший результат:', search_lr.best_score_)


# In[105]:


get_ipython().run_cell_magic('time', '', 'grid_cb.fit(X_train[col_main], y_train)')


# In[106]:


pred_cb = grid_cb.best_estimator_.predict(X_train)
print('Лучший результат:', grid_cb.best_score_)


# На модели LogisticRegression метрика стала чуть хуже, но на Catboost улучшилась. И стало намного быстрее считать!!!
# 
# Предлагаю проверить на признаках из корреляции.

# In[107]:


X_train.head(1)


# In[108]:


col_main_corr = ['PaymentMethod', 
                 'Partner', 'OnlineSecurity', 
                 'OnlineBackup', 'DeviceProtection', 'StreamingTV', 'StreamingMovies', 'MultipleLines']


# In[109]:


num_col_names = ['MonthlyCharges', 'TotalCharges', 'UseTime']


# In[110]:


X = df.drop(['Sign'], axis=1)
y = df['Sign']


# In[111]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=RANDOM_STATE)


# In[112]:


X_train_ohe, X_test_ohe = normal_encoder(X_train[col_main_corr], X_test[col_main_corr], encoder)


# In[113]:


X_train_scaled, X_test_scaled = standard_scaler(X_train, X_test, num_col_names, scaler) 


# In[114]:


X_train = pd.concat([X_train_ohe, X_train_scaled], axis=1).reset_index(drop=True)
X_test = pd.concat([X_test_ohe, X_test_scaled], axis=1).reset_index(drop=True)


# In[115]:


X_train.head(2)


# In[116]:


search_lr.fit(X_train, y_train)


# In[117]:


print('Лучшие параметры:', search_lr.best_params_)
print('Лучший результат:', search_lr.best_score_)


# метрика LogisticRegression стала еще хуже.

# In[118]:


get_ipython().run_cell_magic('time', '', 'grid_cb.fit(X_train, y_train)')


# In[119]:


pred_cb = grid_cb.best_estimator_.predict(X_train)
print('Лучший результат:', grid_cb.best_score_)


# Метрика стала чуть хуже, но зато быстрее считает.

# При любом раскладе метрика изменилась не значительно, но есть смысл экспрементировать так как это приводит к существенному снижению затраченного времени на обучение модели.

# <div class="alert alert-success">
# <b>👍 Успех:</b> Молодец, финальный проект завершен! Сама работа получилась хорошей и структурированной, были предобработаны и проанализированы данные, выбран целевой признак, рассчеты подкреплены визуализацией, это очень важная часть работы, которая облегчает анализ и позволяет полнее представлять происходящее в данных. Построено и обучено несколько моделей, все они оценены и выбрана лучшая. Цель работы достигнута, получена модель хорошо предсказывающая уход клиентов. Не забывай о том, что все пункты очень важны и каждому стоит уделять максимум внимания. <p>
# С опытом становится значительно легче, но опыт это не только повторение однажды изученного, но и постоянное развитие, тем более, что ты выбрал очень динамично развивающуюся область. <p>
# В будущей профессии тебе точно пригодиться умение системно подходить к решению аналитических задач, здесь рекомендую изучить ТРИЗ и системный анализ, из литературы можно почитать Теоретический минимум по Big Data — Су Кеннет и Ын Анналин, Практическая статистика для специалистов Data Science — Брюс П. и Брюс Э., Real-World Machine Learning — Henric Brink, Joseph Мark, W. Richards Fetherolf, Прикладное машинное обучение с помощью Scikit-Learn и TensorFlow — Жерон Орельен.<p>
# Есть интересные сообщества (например https://vk.com/mashinnoe_obuchenie_ai_big_data) и конечно же https://habr.com/ru/all/<p>
# 
# Дополнительно предлагаю посмотреть:
# - Книга от ШАД: https://academy.yandex.ru/handbook/ml
# 
# - Открытый курс машинного обучения: https://habr.com/ru/company/ods/blog/322626/
# 
#  Удачи тебе и профессионального роста!
# </div>

# In[ ]:




