# -*- coding: ISO-8859-2 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "3686382076-Ycyc5oDfyFpUtEV46TcP1faWc3JHaXa1OBF9APs"
access_token_secret = "RgeZbdVff3uv8RXBaNzpFLA9W3x2j4o2g81L6DcZJINYC"
consumer_key = "WGLnKpYsK3hhOYSupYiLVSui5"
consumer_secret = "75NhnD0B2rLP7QKj3bV2Q6ljrn2xtRU3Fjyp5ap2JhfZNScFTH"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(languages=["en"], async=True, track=["colombia university,Massachusetts Institute of Technology,\
    University of Cambridge,Cambridge university,EPFL,KAIST,Korea Advanced Institute of Science & Technology,\
    Harvard University,University College London,University of Oxford,Oxford university,Imperial College London,\
    Yale University,University of Chicago,Chicago university,Princeton University,California Institute of Technology Caltech,\
    Caltech,UCLA,University of Pennsylvania,Pennsylvania university,ETH Zurich,Swiss Federal Institute of Technology,Cornell University,\
    Stanford University,Johns Hopkins University,University of Michigan,Michigan university,McGill University,University of Toronto,\
    University of Warwick,\
     Warwick University,Toronto university,Duke University,University of Edinburgh,UCSD,University of California,Berkeley university,\
     California university,University of Hong Kong,\
     University of New South Wales,UNSW Australia,UNSW,Australian National University,London school of economics and political science,\
     National University of Singapore,\
     NUS,King's College London,Northwestern University,University of Bristol,Nanyang Technological university,University of Tokyo,\
     University of California,\
     University of Los Angeles,los Angeles university,University of Manchester,Manchester university,Hong Kong University of Science and Technology,\
     Hong Kong University of Science and Technology,Hong Kong University,ENS Paris,Kyoto University,University of Melbourne,Melbourne university,\
     Seoul National University,Seoul University,University of Wisconsin-Madison,University of Sydney,Fudan University,Sydney university,\
     Chinese University of Hong Kong,\
     Ecole Polytechnique ParisTech,Brown University,New York University,Peking University,Columbia University,University of British Columbia,\
     British Columbia university,\
     University of Queensland,Nanyang Technological University,Tsinghua University,Carnegie Mellon University,Osaka University,University of Amsterdam,\
     Amsterdam University,\
     Tokyo Institute of Technology,City university of Hong Kong,University of Illinois at Urbana-Champaign,Technische Universitaet Muenchen,Durham University,\
     Carnegie Mellon University,\
     University of Glasgow,Delft University of Technology,University of Washington,Ruprecht-Karls-Universitaet Heidelberg,Monash University,University of St Andrews,\
     University of Copenhagen,\
     University of Nottingham,Lund University,National Taiwan University,Shanghai Jiao Tong University,Tohoku University,Ludwig-Maximilians-Universitaet Muenchen,\
     University of Birmingham,\
     University of Texas at Austin,Trinity College Dublin,University of North Carolina,Chapel Hill university,University of Sheffield,University of Southampton,\
     University of Auckland,KU Leuven,\
     Georgia Institute of Technology,University of Zurich,University of California,Davis university,University of Leeds,Pohang University of Science And Technology,\
     University of Geneva,\
     Purdue University,Boston University,KTH Royal Institute of Technology,Karlsruhe Institute of Technology,Utrecht University,Leiden University,University of Alberta,\
     University of Helsinki,University of Western Australia,Ohio State University,University of Groningen,Pennsylvania State University,\
     Uppsala University,University of York,Korea University,\
     Yonsei University,Rice University,Aarhus University,Lomonosov Moscow State University,Queen Mary University of London,Washington University in St Louis,Zhejiang University,Technical University of Denmark,\
     University of Adelaide,University of Science and Technology of China,Universite de Montreal,Hong Kong Polytechnic University,Eindhoven University of Technology,Sungkyunkwan University,SKKU,\
     Freie Universitaet Berlin,Nagoya University,Lancaster University,Cardiff University,University of Minnesota,Universidad de Buenos Aires,Ghent University,Erasmus University Rotterdam,\
     Humboldt-Universitaet zu Berlin,University of Maryland,College Park university,University of California,Santa Barbara university,University of Southern California,Nanjing University,Chalmers University of Technology,\
     Albert-Ludwigs-Universitaet Freiburg,University of Pittsburgh,Wageningen University,University of OsloNorway,University of Aberdeen,Universite Pierre et Marie Curie,University of Basel,\
     Aalto University,Hokkaido University,Kyushu University,University of Lausanne,Universidade de Sao Paulo,RWTH Aachen University,RWTH,Universiti Malaya,UM Malaysia,Indian Institute of Science,\
     IISc Bangalore,Hebrew University of Jerusalem,Universite Catholique de Louvain,McMaster University,University of Liverpool,University of Waterloo,University of Vienna,University College Dublin,\
     National Tsing Hua University,Ecole Centrale de Paris,University of Reading,Dartmouth College,University of Bath,Texas A&M University,Universidad Nacional Autonoma de Mexico,UNAM,University of Exeter,\
     Newcastle University,University of California Irvine university,Michigan State University,Emory University,University of Bern,University of Barcelona,Georg-August-University Goettingen,Maastricht University,\
     Pontificia Universidad Catolica de Chile,University of Cape Town,University of Virginia,University of Otago,Eberhard Karls Universitaet Tuebingen,University of Colorado Boulder,\
     Vrije Universiteit Amsterdam,Radboud University,Technische Universitaet Berlin,Indian Institute of Technology Delhi,University of Florida,University of Bergen,\
     Queen's University Belfast,National Chiao Tung University,Stockholm University,University of Illinois,Chicago university UIC,Universidad Autonoma de Madrid,University of Sussex,Politecnico di Milano,\
     University of Twente,ecole Normale Superieure de Lyon,University of Rochester,Universitat Autonoma de Barcelona,University of Western Ontario,Hanyang University,Vrije Universiteit Brussel,\
     University of Notre Dame,Universidade estadual de Campinas,Vienna University of Technology,Technion - Israel Institute of Technology,King Fahd University of Petroleum & Minerals"])

