This is a **Handbook for users to run in Qianjiangyuan**.

*Module requirement:*
sudo pip install nltk

*Training Process:*

#pre-process for the input images and captions
python create_input_files.py

#Do the training
python train.py

*Run validation*
python eval.py

*Run model*
python caption.py

