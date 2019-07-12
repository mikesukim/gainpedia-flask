
# BackEnd Stacks

    Webserver = Apache

    WebAppServer = Passenger

    WebApp = Flask

    Deployment Automation = Fabric



# Implementing instruction

	DreamHost Server에는
	이미 Apache가 깔려있고, Passenger도 깔려있을수있게 옵션을 줄수있기때문에

	1. Passenger에 flask를 연결하는 것과(passenger_wsgi.py)
	    dreamhost server 최하위 directory 로 public 이 생성된다 passenger때문에.
	    public directory의 한단계 위에 이파일을 위치시킨다.
	1. flask 앱만 작성하면됨.


# Deployment instruction
	
	1. 내 컴퓨터에 저장되어잇는 myapp을 개발후 
	   확인시에는 python run.py 커멘드로 확인한다
	1. 서버에다가 Deploy 한다
		방법이 여러가지다
		1 FTP 이용하기
		2 Fabric 이용하기
	
		FTP 이용시에 마지막에 서버쪽으로 ssh로 로그인한뒤,
		touch tmp/restart.txt 를 해주어야, Passenger가 app을 다시 로딩한다.



# 무엇을 해야하나
