#-*- coding:utf-8 -*-

class ConstantConfig():

    embedding_size=100     #dimension of word embedding
    vocab_size=8000        #number of vocabulary
    pre_trianing = None   #use vector_char trained by word2vec

    seq_length=600         #max length of sentence
    num_classes=10         #number of labels

    num_filters=128        #number of convolution kernel
    filter_sizes=[2,3,4]   #size of convolution kernel


    keep_prob=0.5          #droppout
    lr= 1e-3               #learning rate
    lr_decay= 0.9          #learning rate decay
    clip= 6.0              #gradient clipping threshold
    l2_reg_lambda=0.01     #l2 regularization lambda

    num_epochs=10          #epochs
    batch_size=64         #batch_size
    print_per_batch =100   #print result

    train_filename='D:\\source_codes\\python\\nlp_process\\text-cnn-master\\data\\cnews.train.txt'  #train data
    test_filename='D:\\source_codes\\python\\nlp_process\\text-cnn-master\\data\\cnews.test.txt'    #test data
    val_filename='D:\\source_codes\\python\\nlp_process\\text-cnn-master\\data\\cnews.val.txt'      #validation data
    vocab_filename='D:\\source_codes\\python\\nlp_process\\text-cnn-master\\data\\vocab.txt'        #vocabulary
    vector_word_filename='D:\\source_codes\\python\\nlp_process\\text-cnn-master\\data\\vector_word.txt'  #vector_word trained by word2vec
    vector_word_npz='D:\\source_codes\\python\\nlp_process\\text-cnn-master\\data\\vector_word.npz'   # save vector_word to numpy file
