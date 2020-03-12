import masscan
import warnings 

warnings.filterwarnings("ignore")


def start_crawling_masscan(ip_address, ip_range, ports, arguments='--max-rate 10000'):
	mas = masscan.PortScanner() 
	mas.scan(f"{ip_address}/{ip_range}", ports=ports, arguments=arguments)
	scan_result = mas.scan_result

	urls=["http://127.0.0.1:8081/",	"http://127.0.0.1:80/"]
	for ip in scan_result['scan']:
		for port in scan_result['scan'][ip]['tcp'].keys():
			url = "https://"
			if port != 443:
				url = "http://"
			url = url+str(ip)+":"+str(port)+"/"
			urls.append(url)

	return urls

def start_crawling(ip_address="192.168.1.1", ip_range="24", ports="80,443,8080,8081", scan_type="masscan"):
	if scan_type == "masscan":
		return start_crawling_masscan(ip_address, ip_range, ports,arguments='--max-rate 100000')


if __name__ == '__main__':
	urls=start_crawling()
	for url in urls:
		print(url)