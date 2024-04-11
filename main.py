# import packages needed
from flask import Flask, render_template, request
import pymongo
import logging


# configure flask
app = Flask(__name__)

# Configure MongoDB connection
mongoClient = pymongo.MongoClient(
    "mongodb+srv://edward:Edward99@assignment.8snc4.mongodb.net/assignment?retryWrites=true&w=majority")
mongoDB = mongoClient['GYMFIT']


# Stores the data into Mongo collection
def store_supplements(email, suppDate, suppOneName, suppTwoName, suppThreeName, suppFourName, suppFiveName,
                      suppOneAmount, suppTwoAmount, suppThreeAmount, suppFourAmount, suppFiveAmount, suppOneMeasurement,
                      suppTwoMeasurement, suppThreeMeasurement, suppFourMeasurement, suppFiveMeasurement):
    collection = mongoDB['Supplements']
    json_data = {"email": email, "suppDate": suppDate, "suppOneName": suppOneName,
                 "suppTwoName": suppTwoName, "suppThreeName": suppThreeName, "suppFourName": suppFourName,
                 "suppFiveName": suppFiveName, "suppOneAmount": suppOneAmount, "suppTwoAmount": suppTwoAmount,
                 "suppThreeAmount": suppThreeAmount, "suppFourAmount": suppFourAmount,
                 "suppFiveAmount": suppFiveAmount, "suppOneMeasurement": suppOneMeasurement,
                 "suppTwoMeasurement": suppTwoMeasurement, "suppThreeMeasurement": suppThreeMeasurement,
                 "suppFourMeasurement": suppFourMeasurement, "suppFiveMeasurement": suppFiveMeasurement}
    collection.insert_one(json_data)


def store_nutrition(email, nutDate, mealNames, calTotal, fdCal10, fdCal9, fdCal8, fdCal7, fdCal6, fdCal5, fdCal4,
                    fdCal3, fdCal2, fdCal1, fdUnit10, fdUnit9, fdUnit8, fdUnit7, fdUnit6, fdUnit5, fdUnit4,
                    fdUnit3, fdUnit2, fdUnit1, fdAmount10, fdAmount9, fdAmount8, fdAmount7, fdAmount6, fdAmount5,
                    fdAmount4, fdAmount3, fdAmount2, fdAmount1, fdItem10, fdItem9, fdItem8, fdItem7, fdItem6,
                    fdItem5, fdItem4, fdItem3, fdItem2, fdItem1):
    collection = mongoDB['Diet']
    json_data = {"email": email, "nutDate": nutDate, "mealNames": mealNames, "calTotal": calTotal, "fdCal10": fdCal10,
                 "fdCal9": fdCal9, "fdCal8": fdCal8, "fdCal7": fdCal7, "fdCal6": fdCal6, "fdCal5": fdCal5,
                 "fdCal4": fdCal4, "fdCal3": fdCal3, "fdCal2": fdCal2, "fdCal1": fdCal1, "fdUnit10": fdUnit10,
                 "fdUnit9": fdUnit9, "fdUnit8": fdUnit8, "fdUnit7": fdUnit7, "fdUnit6": fdUnit6, "fdUnit5": fdUnit5,
                 "fdUnit4": fdUnit4, "fdUnit3": fdUnit3, "fdUnit2": fdUnit2, "fdUnit1": fdUnit1,
                 "fdAmount10": fdAmount10, "fdAmount9": fdAmount9, "fdAmount8": fdAmount8, "fdAmount7": fdAmount7,
                 "fdAmount6": fdAmount6, "fdAmount5": fdAmount5, "fdAmount4": fdAmount4, "fdAmount3": fdAmount3,
                 "fdAmount2": fdAmount2, "fdAmount1": fdAmount1, "fdItem10": fdItem10, "fdItem9": fdItem9,
                 "fdItem8": fdItem8, "fdItem7": fdItem7, "fdItem6": fdItem6, "fdItem5": fdItem5, "fdItem4": fdItem4,
                 "fdItem3": fdItem3, "fdItem2": fdItem2, "fdItem1": fdItem1}
    collection.insert_one(json_data)


def store_workout(email, wrkDate, wrkName, wrkEx1, wrkWeight1, wrkRep1, wrkSet1, wrkNote1, wrkEx2, wrkWeight2,
                  wrkRep2, wrkSet2, wrkNote2, wrkEx3, wrkWeight3, wrkRep3, wrkSet3, wrkNote3, wrkEx4, wrkWeight4,
                  wrkRep4, wrkSet4, wrkNote4, wrkEx5, wrkWeight5, wrkRep5, wrkSet5, wrkNote5, wrkEx6, wrkWeight6,
                  wrkRep6, wrkSet6, wrkNote6, wrkEx7, wrkWeight7, wrkRep7, wrkSet7, wrkNote7, wrkEx8, wrkWeight8,
                  wrkRep8, wrkSet8, wrkNote8, wrkEx9, wrkWeight9, wrkRep9, wrkSet9, wrkNote9, wrkEx10, wrkWeight10,
                  wrkRep10, wrkSet10, wrkNote10):
    collection = mongoDB['Workouts']
    json_data = {"email": email, "wrkDate": wrkDate, "wrkName": wrkName, "wrkEx1": wrkEx1, "wrkWeight1": wrkWeight1,
                 "wrkRep1": wrkRep1, "wrkSet1": wrkSet1, "wrkNote1": wrkNote1, "wrkEx2": wrkEx2,
                 "wrkWeight2": wrkWeight2,
                 "wrkRep2": wrkRep2, "wrkSet2": wrkSet2, "wrkNote2": wrkNote2, "wrkEx3": wrkEx3,
                 "wrkWeight3": wrkWeight3,
                 "wrkRep3": wrkRep3, "wrkSet3": wrkSet3, "wrkNote3": wrkNote3, "wrkEx4": wrkEx4,
                 "wrkWeight4": wrkWeight4,
                 "wrkRep4": wrkRep4, "wrkSet4": wrkSet4, "wrkNote4": wrkNote4, "wrkEx5": wrkEx5,
                 "wrkWeight5": wrkWeight5,
                 "wrkRep5": wrkRep5, "wrkSet5": wrkSet5, "wrkNote5": wrkNote5, "wrkEx6": wrkEx6,
                 "wrkWeight6": wrkWeight6,
                 "wrkRep6": wrkRep6, "wrkSet6": wrkSet6, "wrkNote6": wrkNote6, "wrkEx7": wrkEx7,
                 "wrkWeight7": wrkWeight7,
                 "wrkRep7": wrkRep7, "wrkSet7": wrkSet7, "wrkNote7": wrkNote7, "wrkEx8": wrkEx8,
                 "wrkWeight8": wrkWeight8,
                 "wrkRep8": wrkRep8, "wrkSet8": wrkSet8, "wrkNote8": wrkNote8, "wrkEx9": wrkEx9,
                 "wrkWeight9": wrkWeight9,
                 "wrkRep9": wrkRep9, "wrkSet9": wrkSet9, "wrkNote9": wrkNote9, "wrkEx10": wrkEx10,
                 "wrkWeight10": wrkWeight10,
                 "wrkRep10": wrkRep10, "wrkSet10": wrkSet10, "wrkNote10": wrkNote10}
    collection.insert_one(json_data)


# ------------------Define Routes----------
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/TandC')
def TandC():
    return render_template('TandC.html')


# --------------- Workouts --------------------
@app.route('/wrkView', methods=['GET', 'POST'])
def wrkView():
    if request.method == 'GET':
        return "get method called"
    else:
        collection = mongoDB['Workouts']
        email = request.form['email']
        query = {"email": email}
        data = collection.find(query)
        return render_template('wrkView.html', data=data)



@app.route('/wrkSplash')
def wrkSplash():
    return render_template('wrkSplash.html')


@app.route('/afterWrkSubmit', methods=['GET', 'POST'])
def afterWrkSubmit():
    try:
        if request.method == 'GET':
            return render_template("404.html")
        else:
            email = request.form['email']
            wrkName = request.form['wrkName']
            wrkDate = request.form['wrkDate']

            wrkEx1 = request.form['wrkEx1']
            wrkWeight1 = request.form['wrkWeight1']
            wrkRep1 = request.form['wrkRep1']
            wrkSet1 = request.form['wrkSet1']
            wrkNote1 = request.form['wrkNote1']
            wrkEx2 = request.form['wrkEx2']
            wrkWeight2 = request.form['wrkWeight2']
            wrkRep2 = request.form['wrkRep2']
            wrkSet2 = request.form['wrkSet2']
            wrkNote2 = request.form['wrkNote2']
            wrkEx3 = request.form['wrkEx3']
            wrkWeight3 = request.form['wrkWeight3']
            wrkRep3 = request.form['wrkRep3']
            wrkSet3 = request.form['wrkSet3']
            wrkNote3 = request.form['wrkNote3']

            wrkEx4 = request.form['wrkEx4']
            wrkWeight4 = request.form['wrkWeight4']
            wrkRep4 = request.form['wrkRep4']
            wrkSet4 = request.form['wrkSet4']
            wrkNote4 = request.form['wrkNote4']

            wrkEx5 = request.form['wrkEx5']
            wrkWeight5 = request.form['wrkWeight5']
            wrkRep5 = request.form['wrkRep5']
            wrkSet5 = request.form['wrkSet5']
            wrkNote5 = request.form['wrkNote5']

            wrkEx6 = request.form['wrkEx6']
            wrkWeight6 = request.form['wrkWeight6']
            wrkRep6 = request.form['wrkRep6']
            wrkSet6 = request.form['wrkSet6']
            wrkNote6 = request.form['wrkNote6']

            wrkEx7 = request.form['wrkEx7']
            wrkWeight7 = request.form['wrkWeight7']
            wrkRep7 = request.form['wrkRep7']
            wrkSet7 = request.form['wrkSet7']
            wrkNote7 = request.form['wrkNote7']

            wrkEx8 = request.form['wrkEx8']
            wrkWeight8 = request.form['wrkWeight8']
            wrkRep8 = request.form['wrkRep8']
            wrkSet8 = request.form['wrkSet8']
            wrkNote8 = request.form['wrkNote8']

            wrkEx9 = request.form['wrkEx9']
            wrkWeight9 = request.form['wrkWeight9']
            wrkRep9 = request.form['wrkRep9']
            wrkSet9 = request.form['wrkSet9']
            wrkNote9 = request.form['wrkNote9']

            wrkEx10 = request.form['wrkEx10']
            wrkWeight10 = request.form['wrkWeight10']
            wrkRep10 = request.form['wrkRep10']
            wrkSet10 = request.form['wrkSet10']
            wrkNote10 = request.form['wrkNote10']

            store_workout(email, wrkDate, wrkName, wrkEx1, wrkWeight1, wrkRep1, wrkSet1, wrkNote1, wrkEx2, wrkWeight2,
                          wrkRep2, wrkSet2, wrkNote2, wrkEx3, wrkWeight3, wrkRep3, wrkSet3, wrkNote3, wrkEx4, wrkWeight4,
                          wrkRep4, wrkSet4, wrkNote4, wrkEx5, wrkWeight5, wrkRep5, wrkSet5, wrkNote5, wrkEx6, wrkWeight6,
                          wrkRep6, wrkSet6, wrkNote6, wrkEx7, wrkWeight7, wrkRep7, wrkSet7, wrkNote7, wrkEx8, wrkWeight8,
                          wrkRep8, wrkSet8, wrkNote8, wrkEx9, wrkWeight9, wrkRep9, wrkSet9, wrkNote9, wrkEx10, wrkWeight10,
                          wrkRep10, wrkSet10, wrkNote10)

            return render_template('afterWrkSubmit.html', email=email, wrkDate=wrkDate, wrkName=wrkName, wrkEx1=wrkEx1,
                                   wrkWeight1=wrkWeight1, wrkRep1=wrkRep1, wrkSet1=wrkSet1, wrkNote1=wrkNote1,
                                   wrkEx2=wrkEx2, wrkWeight2=wrkWeight2, wrkRep2=wrkRep2, wrkSet2=wrkSet2,
                                   wrkNote2=wrkNote2, wrkEx3=wrkEx3, wrkWeight3=wrkWeight3, wrkRep3=wrkRep3,
                                   wrkSet3=wrkSet3, wrkNote3=wrkNote3, wrkEx4=wrkEx4, wrkWeight4=wrkWeight4,
                                   wrkRep4=wrkRep4, wrkSet4=wrkSet4, wrkNote4=wrkNote4, wrkEx5=wrkEx5,
                                   wrkWeight5=wrkWeight5, wrkRep5=wrkRep5, wrkSet5=wrkSet5, wrkNote5=wrkNote5,
                                   wrkEx6=wrkEx6, wrkWeight6=wrkWeight6, wrkRep6=wrkRep6, wrkSet6=wrkSet6,
                                   wrkNote6=wrkNote6, wrkEx7=wrkEx7, wrkWeight7=wrkWeight7, wrkRep7=wrkRep7,
                                   wrkSet7=wrkSet7, wrkNote7=wrkNote7, wrkEx8=wrkEx8, wrkWeight8=wrkWeight8,
                                   wrkRep8=wrkRep8, wrkSet8=wrkSet8, wrkNote8=wrkNote8, wrkEx=wrkEx9, wrkWeight9=wrkWeight9,
                                   wrkRep9=wrkRep9, wrkSet9=wrkSet9, wrkNote9=wrkNote9, wrkEx10=wrkEx10,
                                   wrkWeight10=wrkWeight10, wrkRep10=wrkRep10, wrkSet10=wrkSet10, wrkNote10=wrkNote10)
    except KeyError as e:
        return render_template('keyError.html', e=e)


@app.route('/wrkDelete')
def wrkDelete():
    return render_template('wrkDelete.html')


@app.route('/afterWrkDelete', methods=['GET', 'POST'])
def afterWrkDelete():
    try:
        if request.method == 'GET':
            return render_template("404.html")
        else:
            email = request.form['email']
            wrkDate = request.form['wrkDate']
            collection = mongoDB['Workouts']
            query = {"$and": [{"email": email}, {"wrkDate": wrkDate}]}
            collection.delete_one(query)
            return render_template("afterWrkDelete.html", email=email, wrkDate=wrkDate)
    except KeyError as e:
        return render_template('keyError.html', e=e)


# --------------- Supplements --------------------
@app.route('/suppView', methods=['GET', 'POST'])
def suppView():
    if request.method == 'GET':
        return "get method called"
    else:
        collection = mongoDB['Supplements']
        email = request.form['email']
        query = {"email": email}
        data = collection.find(query)
        return render_template('suppView.html', data=data)


@app.route('/suppSplash')
def suppSplash():
    return render_template('suppSplash.html')


@app.route('/afterSuppSubmit', methods=['GET', 'POST'])
def afterSuppSubmit():
    try:
        if request.method == 'GET':
            return render_template("404.html")
        else:
            email = request.form['email']
            suppDate = request.form['suppDate']
            suppOneName = request.form['suppOneName']
            suppOneAmount = request.form['suppOneAmount']
            suppOneMeasurement = request.form['suppOneMeasurement']
            suppTwoName = request.form['suppTwoName']
            suppTwoAmount = request.form['suppTwoAmount']
            suppTwoMeasurement = request.form['suppTwoMeasurement']
            suppThreeName = request.form['suppThreeName']
            suppThreeAmount = request.form['suppThreeAmount']
            suppThreeMeasurement = request.form['suppThreeMeasurement']
            suppFourName = request.form['suppFourName']
            suppFourAmount = request.form['suppFourAmount']
            suppFourMeasurement = request.form['suppFourMeasurement']
            suppFiveName = request.form['suppFiveName']
            suppFiveAmount = request.form['suppFiveAmount']
            suppFiveMeasurement = request.form['suppFiveMeasurement']

            store_supplements(email, suppDate, suppOneName, suppTwoName, suppThreeName, suppFourName, suppFiveName,
                              suppOneAmount, suppTwoAmount, suppThreeAmount, suppFourAmount, suppFiveAmount,
                              suppOneMeasurement, suppTwoMeasurement, suppThreeMeasurement, suppFourMeasurement,
                              suppFiveMeasurement)

            return render_template('afterSuppSubmit.html', email=email, suppDate=suppDate, suppOneName=suppOneName,
                                   suppTwoName=suppTwoName, suppThreeName=suppThreeName, suppFourName=suppFourName,
                                   suppFiveName=suppFiveName, suppOneAmount=suppOneAmount, suppTwoAmount=suppTwoAmount,
                                   suppThreeAmount=suppThreeAmount, suppFourAmount=suppFourAmount,
                                   suppFiveAmount=suppFiveAmount, suppOneMeasurement=suppOneMeasurement,
                                   suppTwoMeasurement=suppTwoMeasurement, suppThreeMeasurement=suppThreeMeasurement,
                                   suppFourMeasurement=suppFourMeasurement, suppFiveMeasurement=suppFiveMeasurement)
    except KeyError as e:
        return render_template('keyError.html', e=e)


@app.route('/suppDelete')
def suppDelete():
    return render_template('suppDelete.html')


@app.route('/afterSuppDelete', methods=['GET', 'POST'])
def afterSuppDelete():
    try:
        if request.method == 'GET':
            return render_template("404.html")
        else:
            email = request.form['email']
            suppDate = request.form['suppDate']
            collection = mongoDB['Supplements']
            query = {"$and": [{"email": email}, {"suppDate": suppDate}]}
            collection.delete_one(query)
            return render_template("afterSuppDelete.html", email=email, suppDate=suppDate)
    except KeyError as e:
        return render_template('keyError.html', e=e)


# --------------- Nutrition --------------------
@app.route('/nutView', methods=['GET', 'POST'])
def nutView():
    try:
        if request.method == 'GET':
            return "get method called"
        else:
            collection = mongoDB['Diet']
            email = request.form['email']
            query = {"email": email}
            data = collection.find(query)
            return render_template('nutView.html', data=data)
    except KeyError as e:
        return render_template('keyError.html', e=e)


@app.route('/nutSplash')
def nutSplash():
    return render_template('nutSplash.html')


@app.route('/afterNutSubmit', methods=['GET', 'POST'])
def afterNutSubmit():
    try:
        if request.method == 'GET':
            return render_template("404.html")
        else:
            email = request.form['email']
            mealNames = request.form['mealNames']
            nutDate = request.form['nutDate']
            fdItem1 = request.form['fdItem1']
            fdAmount1 = request.form['fdAmount1']
            fdUnit1 = request.form['fdUnit1']
            fdCal1 = request.form['fdCal1']
            fdItem2 = request.form['fdItem2']
            fdAmount2 = request.form['fdAmount2']
            fdUnit2 = request.form['fdUnit2']
            fdCal2 = request.form['fdCal2']
            fdItem3 = request.form['fdItem3']
            fdAmount3 = request.form['fdAmount3']
            fdUnit3 = request.form['fdUnit3']
            fdCal3 = request.form['fdCal3']
            fdItem4 = request.form['fdItem4']
            fdAmount4 = request.form['fdAmount4']
            fdUnit4 = request.form['fdUnit4']
            fdCal4 = request.form['fdCal4']
            fdItem5 = request.form['fdItem5']
            fdAmount5 = request.form['fdAmount5']
            fdUnit5 = request.form['fdUnit5']
            fdCal5 = request.form['fdCal5']
            fdItem6 = request.form['fdItem6']
            fdAmount6 = request.form['fdAmount6']
            fdUnit6 = request.form['fdUnit6']
            fdCal6 = request.form['fdCal6']
            fdItem7 = request.form['fdItem7']
            fdAmount7 = request.form['fdAmount7']
            fdUnit7 = request.form['fdUnit7']
            fdCal7 = request.form['fdCal7']
            fdItem8 = request.form['fdItem8']
            fdAmount8 = request.form['fdAmount8']
            fdUnit8 = request.form['fdUnit8']
            fdCal8 = request.form['fdCal8']
            fdItem9 = request.form['fdItem9']
            fdAmount9 = request.form['fdAmount9']
            fdUnit9 = request.form['fdUnit9']
            fdCal9 = request.form['fdCal9']
            fdItem10 = request.form['fdItem10']
            fdAmount10 = request.form['fdAmount10']
            fdUnit10 = request.form['fdUnit10']
            fdCal10 = request.form['fdCal10']
            calTotal = fdCal1 + fdCal2 + fdCal3 + fdCal4 + fdCal5 + fdCal6 + fdCal7 + fdCal8 + fdCal9 + fdCal10

            store_nutrition(email, nutDate, mealNames, calTotal, fdCal10, fdCal9, fdCal8, fdCal7, fdCal6, fdCal5, fdCal4,
                            fdCal3, fdCal2, fdCal1, fdUnit10, fdUnit9, fdUnit8, fdUnit7, fdUnit6, fdUnit5, fdUnit4,
                            fdUnit3, fdUnit2, fdUnit1, fdAmount10, fdAmount9, fdAmount8, fdAmount7, fdAmount6, fdAmount5,
                            fdAmount4, fdAmount3, fdAmount2, fdAmount1, fdItem10, fdItem9, fdItem8, fdItem7, fdItem6,
                            fdItem5, fdItem4, fdItem3, fdItem2, fdItem1)

            return render_template('afterNutSubmit.html', mealNames=mealNames, email=email, nutDate=nutDate,
                                   calTotal=calTotal, fdCal10=fdCal10, fdCal9=fdCal9, fdCal8=fdCal8, fdCal7=fdCal7,
                                   fdCal6=fdCal6, fdCal5=fdCal5, fdCal4=fdCal4, fdCal3=fdCal3, fdCal2=fdCal2, fdCal1=fdCal1,
                                   fdUnit10=fdUnit10, fdUnit9=fdUnit9, fdUnit8=fdUnit8, fdUnit7=fdUnit7, fdUnit6=fdUnit6,
                                   fdUnit5=fdUnit5, fdUnit4=fdUnit4, fdUnit3=fdUnit3, fdUnit2=fdUnit2, fdUnit1=fdUnit1,
                                   fdAmount10=fdAmount10, fdAmount9=fdAmount9, fdAmount8=fdAmount8, fdAmount7=fdAmount7,
                                   fdAmount6=fdAmount6, fdAmount5=fdAmount5, fdAmount4=fdAmount4, fdAmount3=fdAmount3,
                                   fdAmount2=fdAmount2, fdAmount1=fdAmount1, fdItem10=fdItem10, fdItem9=fdItem9,
                                   fdItem8=fdItem8, fdItem7=fdItem7, fdItem6=fdItem6, fdItem5=fdItem5, fdItem4=fdItem4,
                                   fdItem3=fdItem3, fdItem2=fdItem2, fdItem1=fdItem1)
    except KeyError as e:
        return render_template('keyError.html', e=e)


@app.route('/nutDelete')
def nutDelete():
    return render_template('nutDelete.html')


@app.route('/afterNutDelete', methods=['GET', 'POST'])
def afterNutDelete():
    try:
        if request.method == 'GET':
            return render_template("404.html")
        else:
            email = request.form['email']
            nutDate = request.form['nutDate']
            mealNames = request.form['mealNames']
            collection = mongoDB['Diet']
            query = {"$and": [{"email": email}, {"mealNames": mealNames}, {"nutDate": nutDate}]}
            collection.delete_one(query)
            return render_template("afterSuppDelete.html", email=email, nutDate=nutDate)
    except KeyError as e:
        return render_template('keyError.html', e=e)


# ------------------Error Handlers----------
@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

@app.route('/keyError')
def keyError():
    return render_template('keyError.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
