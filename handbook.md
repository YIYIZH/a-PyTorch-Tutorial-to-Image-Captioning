This is a **Handbook for users to run in Qianjiangyuan**.

### Module requirement:  
*sudo pip install nltk*

### pre-process for the input images and captions 
*python create_input_files.py*

### Do the training 
*python train.py*

### Run validation
*python eval.py*

### Run model
*python caption.py -i path-to-image -m './BEST_checkpoint_coco_5_cap_per_img_5_min_word_freq.pth.tar'
-wm '/dlwsdata2/public/coco/output/WORDMAP_coco_5_cap_per_img_5_min_word_freq.json'*

parser.add_argument('--img', '-i', help='path to image')   
parser.add_argument('--model', '-m', help='path to model')   
parser.add_argument('--word_map', '-wm', help='path to word map JSON')   
parser.add_argument('--beam_size', '-b', default=5, type=int, help='beam size for beam search')   
parser.add_argument('--dont_smooth', dest='smooth', action='store_false', help='do not smooth alpha overlay')
