import media
import fresh_tomatoes

toyStory = media.Movie('Toy Story',
                       "A story about a boy and his toys that come to life",
                       "http://i1.wp.com/img.funtop.tw/2013/05/130505-APP-Toy-Story-Smash-It/APP-Toy-Story-Smash-It_1.jpg",
                       "http://www.renrendai.com")
avatar = media.Movie('Avatar',
                       "A marine on an alien planet",
                       "http://img3.imgtn.bdimg.com/it/u=189163517,1509353584&fm=26&gp=0.jpg",
                       "http://www.renrendai.com")
#avatar.showTrailer()

eightEvil = media.Movie("The Hateful Eight",
                        "A story about eight bad persons",
                        "http://i-7.vcimg.com/crop/160ecbe7a0835bd1cf0bdef7c5de7846121755%28600x%29/thumb.jpg",
                        "http://www.iqiyi.com/v_19rrkq6y14.html?vfm=m_127_bdbk")
#eightEvil.showTrailer()

movies = [toyStory, avatar, eightEvil]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
