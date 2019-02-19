import random
import sys

start = {'bitcoins': 10000, 'staff': 100, 'shops': 5, 'gigabytes': 10000, 'working conditions': 95, 'quarter': 0}
tech = 0


def selling():
    """Information about selling"""
    price1 = random.randint(20, 35)
    buyers = 'Люди готовы купить 1 Гб информации за', price1, 'биткойнов. Сколько Гб продать?'
    print(*buyers)
    amount1 = int(input())
    _max1 = start.get('gigabytes', [])
    update2 = {'bitcoins': start.get('bitcoins', []) + amount1 * price1,
               'gigabytes': start.get('gigabytes', []) - amount1}
    update3 = {'bitcoins': start.get('bitcoins', []) + _max1 * price1,
               'gigabytes': start.get('gigabytes', []) - _max1}
    if amount1 <= start.get('gigabytes', []):
        start.update(update2)
    else:
        print('Вы не можете столько продать, максимум:', _max1)
        start.update(update3)


def buying():
    """Information about buying"""
    price = random.randint(20, 35)
    sellers = 'На сегодняшний день 1 Гб хранилища на флешках продается за', price, 'биткойнов. Сколько Гб купить?'
    print(*sellers)
    amount = int(input())
    _max = start.get('bitcoins', []) // price
    update = {'bitcoins': start.get('bitcoins', []) - amount * price, 'gigabytes': start.get('gigabytes', []) + amount}
    update1 = {'bitcoins': start.get('bitcoins', []) - _max * price, 'gigabytes': start.get('gigabytes', []) + _max}
    if amount * price < start.get('gigabytes', []):
        start.update(update)
    else:
        print('Вы не можете столько купить, максимум:', _max)
        start.update(update1)


def investments():
    """Investments in new technologies"""
    inv = 'Сколько Гб вы хотите инвестировать в разработку новых информационных технологий?'
    print(inv)
    gb = int(input())
    _max2 = start.get('gigabytes', [])
    update4 = {'gigabytes': start.get('gigabytes', []) - gb}
    update5 = {'gigabytes': 0}
    if gb <= _max2:
        start.update(update4)
        global tech
        tech += gb
    else:
        print('Вы не можете столько инвестировать, максимум:', _max2)
        start.update(update5)
        tech += _max2


def salaries():
    """Information about salaries"""
    question = 'Сколько биткойнов выделить на зарплату рабочим?'
    print(question)
    rand0 = random.randint(31, 70)
    rand1 = random.randint(0, 30)
    sal = int(input())
    start1 = start.copy()
    _max3 = start.get('bitcoins', [])
    update6 = {'bitcoins': start.get('bitcoins', []) - sal}
    update7 = {'bitcoins': 0}
    update8 = {'working conditions': start.get('working conditions', []) - rand0}
    update9 = {'working conditions': start.get('working conditions', []) - rand1}
    update10 = {'working conditions': start.get('working conditions', []) + rand1}
    update11 = {'working conditions': start.get('working conditions', []) + rand0}
    if sal <= _max3:
        start.update(update6)
    else:
        print('Вы не можете столько заплатить, максимум:', _max3)
        start.update(update7)
    checking = start1.get('bitcoins', []) - start.get('bitcoins', [])
    if 0 <= checking <= 1000:
        start.update(update8)
    elif 1001 <= checking <= 5000:
        start.update(update9)
    elif 5001 <= checking <= 8000:
        start.update(update10)
    elif checking >= 8001:
        start.update(update11)


def chance_of_act():
    """Appearance of random acts"""
    rand = random.randint(1, 2)
    if rand == 1:
        random_acts()


def staff():
    """Changings of staff"""
    rand = random.randint(30, 80)
    rand1 = random.randint(1, 30)
    update = {'staff': start.get('staff', []) - rand}
    update1 = {'staff': start.get('staff', []) - rand1}
    update2 = {'staff': start.get('staff', []) + rand}
    if start.get('working conditions', []) <= 40:
        start.update(update)
    elif 41 <= start.get('working conditions', []) <= 80:
        start.update(update1)
    elif 100 <= start.get('working conditions', []):
        start.update(update2)


def random_inv():
    """Success of investments"""
    rand = random.randint(1, 2)
    rand1 = random.randint(2, 3)
    global tech
    update = {'gigabytes': start.get('gigabytes', []) + tech * rand1}
    if rand == 1:
        print('Информационные инвестиции оказались удачными в этом квартале')
        start.update(update)
    else:
        print('Информационные инвестиции оказались неудачными в этом квартале')


def loss():
    """Checking of working conditions"""
    if start.get('working conditions', []) <= 0:
        print('Никто не хочет работать в вашей компании. Игра окончена.')
        sys.exit()
    if start.get('shops', []) <= 0:
        print('Все ваши магазины закрыты. Игра окончена')
        sys.exit()
    if start.get('staff', []) <= 0:
        print('Все работники ушли от вас. Игра окончена')
        sys.exit()


def counter():
    """Counting quarters"""
    update = {'quarter': start.get('quarter', []) + 1}
    start.update(update)


def random_1():
    situation = 'К вам с проверкой пришли из МВД,  и непрозрачно намекают на взятку. Сколько биткоинов им дать?'
    print(situation)
    money = int(input())
    _max3 = start.get('bitcoins', [])
    update6 = {'bitcoins': start.get('bitcoins', []) - sal}
    update7 = {'bitcoins': 0}
    minimum = start.get('bitcoins', []) * 0.1
    if money < _max3:
        start.update(update6)
        if money < int(minimum):
            close = start.get('shops', []) * 0.25 + 1
            update = {'shops': start.get('shops', []) - int(close)}
            start.update(update)
        else:
            update1 = {'bitcoins': start.get('bitcoins', []) - money}
            start.update(update1)
    else:
        print('Вы не можете столько инвестировать, максимум:', _max3)
        start.update(update7)


def random_2():
    gb = random.randint(100, 500)
    low_cond = random.randint(5, 10)
    print('{} {} {}'.format('У вас на складе скопилось', gb,
                          'неиспользованных гигабайт. Раздать рабочим?(напишите да или нет'))
    answer = input()
    if answer == 'да':
        cond = {'working conditions': start.get('working conditions', []) + low_cond}
        print('Сотрудники вам благодарны!')
        start.update(cond)
    else:
        new_gb = {'gigabytes': start.get('gigabytes') + gb}
        start.update(new_gb)
        cond1 = {'working conditions': start.get('working conditions', []) - low_cond}
        print('Сотрудники узнали, что вы жмот!')
        start.update(cond1)


def random_3():
    gb = random.randint(700, 2000)
    print('{} {} {}'.format('О нет! Склад с вашими флешками ограбили! Вы потеряли', gb, 'гигабайт!'))
    b = input('Полиция не очень охотно расследует дело. Вы можете нанять частого детектива (да/нет)')
    stolen = {'gigabytes': start.get('gigabytes') - gb}
    start.update(stolen)
    if b == 'да':
        print('Вам предлагается выбор из 3ёх детективов.')
        print('1. Борис Грачевский. Профессионал своего дела, выгнали из участка из-за излишней профессиональности.\n '
              'Гроза преступного мира, известный как "Бетмен за лупой".\nЦена за услуги 4000 бетховенов.')
        print('2. Леонид Перевалов. Бывший морпех, агрессивный, не всегда устойчив психикой, но если дело его\n '
              'заинтересует можете быть уверенны в его выполнении. Имеет судимость по статье о продаже наркотиков.\n'
              'Сам Леонид отрицает решение суда о признании его виновным.\nЦена за услуги 2000 бетховенов.')
        print('3. Никита Скоробей. Студент факультета естественных наук, оставивший предложение на YouDo.\n'
              'Участник шоу "Битва экстрасенсов". В университете Никиту считают странным. В детстве увлекался\n'
              ' дедукцией и вполне успешно расследовал преступления по заказу местных пивнушек.\n'
              'Цена за услуги 200 бетховенов и полторы бутылочки пива.')
        c = int(input('Напишите номер выбранного детектива:'))
        if c == 1:
            cost1 = {'bitcoins': start.get('bitcoins', []) - 4000}
            start.update(cost1)
            d = random.randint(1, 6)
            if d == 6:
                print('К сожалению Борис Грачевский посадил в тюрьму слишком серьёзных людей.\nНа него было совершено '
                      'покушение и он скончался в больнице.\nВаше дело он не закончил.')
            else:
                back = {'gigabytes': start.get('gigabytes') + gb}
                start.update(back)
                print('Борис Грачевский за 9 минут раскрыл ваше дело и вышел на мафиозного авторитета.\n'
                      'Все ваши гигабайты вернулись')
        elif c == 2:
            cost2 = {'bitcoins': start.get('bitcoins', []) - 2000}
            start.update(cost2)
            e = random.randint(1, 6)
            if e >= 5:
                back2 = {'gigabytes': start.get('gigabytes') + 40}
                start.update(back2)
                print('Леонид оказался ярым ненавистником интернета, но за дело взялся. Однако пока он боролся\n'
                      'со своим нежеланием работать на благо мировой паутины, злоумышленники успели сбыть\n'
                      'весь товар. На их базе было найдено только 4 флешки.')
            elif e == 4:
                back3 = {'gigabytes': start.get('gigabytes') + gb / 2}
                start.update(back3)
                print('Дело раскрыли слишком поздно и половину ваших флешек успели сбыть.')
            else:
                back4 = {'gigabytes': start.get('gigabytes') + gb}
                start.update(back4)
                print('Леонид расскрыл дело. Преступниками оказалась конкурирующая компания.')
        else:
            cost3 = {'bitcoins': start.get('bitcoins', []) - 202}
            start.update(cost3)
            f = random.randint(1, 6)
            if f >= 3:
                bn = {'bitcoins': start.get('bitcoins', []) + 200}
                start.update(bn)
                print('Как ни странно Никита вышел на преступную организацию, но к сожалению они взяли его в плен и\n'
                      'жестоко пытали. После того как его отпустили, Никита отказывался говорить из-за страха\n'
                      'снова там оказаться. Он вернул вам все деньги, кроме денег за пиво.')
            elif f == 2:
                print('Никита оказывается главой преступной организации, которая обокрала вас.\nОн пропал навсегда. По '
                      'слухам уехал в Мексику')
            else:
                print('ЧТО? Никита Скоробей справился с заданием. Его детективный ум прославился на всю страну и его '
                      'наняло на работу агенство Бориса Грачевского')
    else:
        print('Попрощайтесь с флешками!')


def random_4():
    gb = random.randint(1000, 8000)
    loose = {'gigabytes': start.get('gigabytes') - gb}
    start.update(loose)
    print('{} {} {}'.format('Ваша система подверглась заражению! Вы потеряли', gb, 'гигабайт!'))


def random_5():
    gb = random.randint(500, 1000)
    loose = {'gigabytes': start.get('gigabytes') - gb}
    start.update(loose)
    print('{} {} {}'.format('К вам приехала бракованная партия флешек! Вы потеряли', gb, 'гигабайт'))


def random_6():
    take = {'gigabytes': start.get('gigabytes') + 1000}
    start.update(take)
    print('Сюрприз! Ваши партнёры из Мвидео поздравили вас с годом плодотворного сотрудничества и подарили 1000 Гб')

def random_7():
    bit = random.randrange(5000,35000,100)
    print('{} {} {}''Прекрасные новости! Освободилось место, которое вы давно присматривали для своего магазина.\n'
          'Стоимость -', bit, 'биткоинов')
    b = input('Покупаете?(да/нет):')
    if b == 'да':
        take = {'bitcoins': start.get('bitcoins', []) - bit}
        start.update(take)
        print('Поздравляем с покупкой!')

def random_8():
    print('Один из ваших магазинов подвергся рекетскому нападению, вы теряете магазин. Ничего не поделаешь\n'
          'в такое уж время мы живём((')
    b = {'shops': start.get('shops', []) - 1}
    start.update(b)

def random_9():
    print('Умер ваш богатый родственник...\n'
          'В завещании написано, что все деньги достаются вам!')
    bill = {'bitcoins':start.get('bitcoins')+10000}
    start.update(bill)

def random_10():
    cost = random.randrange(10000, 30000, 100)
    print('На вас подали в суд за пиратство! Придётся нанять адвоката!')
    print('Стоимость его услуг - ', cost)
    answ = input('Нанять адвоката?(да/нет)')
    if answ == 'да':
        if start.get('bitcoins') >= cost:
            chance = random.randint(1,6)
            pay = {'bitcoins':start.get('bitcoins') - cost}
            start.update(pay)
            if chance >=4:
                print('Вы проиграли дело!')
                rand = random.randint(50, 100)
                rand1 = random.randint(1, 5)
                update1 = {'staff': start.get('staff') - rand, 'shops': start.get('shops') - rand1,
                           'working conditions': start.get('working conditions') - 50}
            else:
                print('Вы выиграли дело!')
        else:
            print('У вас недостаточно биткоинов')
            b = input('Вложить все оставшиеся в адвоката?')
            if b == 'да':
                pay1 = {'bitcoins': start.get('bitcoins') - start.get('bitcoins')}
                start.update(pay1)
                ch = random.randint(1,6)
                if ch >=4:
                    print('Вы проиграли дело!')
                    ra = random.randint(50, 100)
                    ra1 = random.randint(1, 5)
                    update1 = {'staff': start.get('staff') - ra, 'shops': start.get('shops') - ra1,
                           'working conditions': start.get('working conditions') - 50}
                    start.update(update1)
                else:
                    print('Вы выиграли дело!')
            elif b == 'нет':
                print('Вы проиграли дело!')
                ran = random.randint(50, 100)
                ran1 = random.randint(1, 5)
                up = {'staff': start.get('staff') - ran, 'shops': start.get('shops') - ran1,
                           'working conditions': start.get('working conditions') - 50}
                start.update(up)
    if answ == 'нет':
        print('Вы проиграли дело!')
        ranty = random.randint(50, 100)
        ranty1 = random.randint(1, 5)
        upty = {'staff': start.get('staff') - ranty, 'shops': start.get('shops') - ranty1,
              'working conditions': start.get('working conditions') - 50}
        start.update(upty)

def random_acts():
    rand = random.randint(1, 10)
    if rand == 1:
        random_1()
    elif rand == 2:
        random_2()
    elif rand == 3:
        random_3()
    elif rand == 4:
        random_4()
    elif rand == 5:
        random_5()
    elif rand == 6:
        random_6()
    elif rand == 7:
        random_7()
    elif rand == 8:
        random_8()
    elif rand == 9:
        random_9()
    elif rand == 10:
        random_10()
def menu():
    print('|{0:^12} | {1:^12} | {2:^12} | {3:^12} | {4:^12} | {5:^12}|'.format('Биткойны', 'Сотрудники', 'Магазины',
                                                                               'Гигабайты', 'Условия работы',
                                                                               'Квартал'))
    print('|{0:^12} | {1:^12} | {2:^12} | {3:^12} | {4:^14} | {5:^12}|'
          .format(start.get('bitcoins'), start.get('staff'), start.get('shops'), start.get('gigabytes'),
                  start.get('working conditions'), start.get('quarter')))


menu()
selling()
menu()
buying()
menu()
investments()
menu()
salaries()
menu()
chance_of_act()
random_inv()
staff()
menu()
loss()
counter()
