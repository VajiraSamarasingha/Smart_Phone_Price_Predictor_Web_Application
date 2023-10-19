from flask import Flask, render_template,request
import pickle
import datetime
app = Flask(__name__)

def prediction(list):
    filename = 'predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file) 
    pred_value = model.predict([list])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    pred =0
    if request.method == 'POST':
        ram = request.form['ram']
        romstorage = request.form['romstorage']
        frontcamera = request.form['frontcamera']
        phonename = request.form['phonename']
        processor = request.form['processor']
        backcamera = request.form['Back/Rare Camera']
        rate = request.form['rating']
        nrate = request.form['Number of Ratings']
        Battary = request.form['battary']
        
        

        print(ram,romstorage,frontcamera,phonename,processor,backcamera,rate,nrate,Battary)

        feature_list = []
        feature_list.append(int(ram))
        feature_list.append(int(romstorage))
        feature_list.append(int(frontcamera))
        #feature_list.append(processor)
        #feature_list.append(backcamera)
        feature_list.append(int(rate))
        feature_list.append(int(nrate))
        feature_list.append(int(Battary))
        

        Pname_list = ['Other','OnePlus 10R 5G (Sierra Black, 256 GB)','Nokia 3310 DS 2020','Nokia 8210 4G','OnePlus Nord CE 2 5G (Bahama Blue, 128 GB)','SAMSUNG Guru Music 2']
        processor_list = ['Other','Qualcomm Snapdragon 680 Processor','Qualcomm Snapdragon 778G Processor','Mediatek Helio P35 Processor','Unisoc T612 Processor','Mediatek Dimensity 920 Processor','Qualcomm Snapdragon 870 Processor','Qualcomm Snapdragon 695 Processor','Qualcomm Snapdragon 439 Processor']
        backcam = ['Other','50MP Rear Camera','13MP Rear Camera','13MP + 2MP','12MP + 12MP','50MP + 2MP + 2MP','8MP Rear Camera','64MP + 8MP + 2MP','50MP + 2MP','12MP Rear Camera ','13MP + 2MP + 2MP','50MP + 8MP + 2MP','48MP + 2MP + 2MP','48MP Rear Camera','0.3MP Rear Camera','64MP Rear Camera']

        

        def traverse(lst,value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
        
        traverse(Pname_list,phonename)
        traverse(processor_list,processor)
        traverse(backcam,backcamera)

        pred = prediction(feature_list)

        
    return render_template('index.html',pred = pred)


if __name__ == '__main__':
    app.run(debug=True)