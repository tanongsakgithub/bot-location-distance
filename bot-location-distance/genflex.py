import json
def flexagain():
	flex = {"type": "bubble","size": "kilo","body": 
		 {"type": "box","layout": "vertical","spacing": "sm","contents": [
	  {"type": "box","layout": "vertical","contents": [
		  {"type": "text","text": "โปรดส่งตำแหน่งที่ตั้ง","size": "lg","align": "center","contents": []
		  }
		]
	  },
	  {"type": "box","layout": "vertical","margin": "lg","contents": [
		  {"type": "button","action": {"type": "uri","label": "ส่งตำแหน่งปัจจุบัน","uri": "https://line.me/R/nv/location/"},
			"flex": 1,"color": "#00A1FF","style": "primary","gravity": "center"
		  }
		]
	  }
	]
  }
}
	return flex
def bubble(name,image,address,neighborhood,price,url,distance):
	bubble = {
  "type": "bubble",
  "hero": {
	"type": "image",
	"url": str(image),
	"size": "full",
	"aspectRatio": "20:13",
	"aspectMode": "cover"
  },
  "body": {
	"type": "box",
	"layout": "vertical",
	"spacing": "sm",
	"contents": [
	  {"type": "text","text": str(name),"weight": "bold","size": "xl","wrap": True,"contents": []},
	  {"type": "box","layout": "baseline","contents": [
		{"type": "text","text": "฿ "+str(price),"weight": "bold","size": "xl","flex": 0,"wrap": True,"contents": []}
		]
	  },
	  {"type": "box","layout": "vertical","contents": [
		  {"type": "box","layout": "baseline","margin": "md","contents": [
			  {"type": "text","text": "ใกล้ "+str(neighborhood),"color": "#434343FF","contents": []}
			]
		  },
		  {"type": "box","layout": "baseline","margin": "md","contents": [
			{"type": "text","text": "ระยะห่าง","color": "#757575FF","flex": 0,"wrap": True,"contents": []},
			{"type": "text","text": "ประมาณ "+str(distance)+" กิโลเมตร","color": "#757575FF","flex": 0,"margin": "xl","wrap": True,"contents": []}
			]
		  },
		  {"type": "box","layout": "baseline","margin": "md","contents": [
			{"type": "text","text": "ที่อยู่","color": "#757575FF","flex": 0,"wrap": True,"contents": []},
			{"type": "text","text": str(address),"color": "#757575FF","flex": 0,"margin": "xl","wrap": True,"contents": []}
			]
		  }
		]
	  }
	]
  },
  "footer": {
	"type": "box",
	"layout": "vertical",
	"spacing": "sm",
	"contents": [
	  {"type": "button","action": 
		{"type": "uri","label": "รายละเอียดเพิ่มเติม","uri": str(url)},
		
		"style": "secondary"
	  },
	  {"type": "button","action": 
		{"type": "uri","label": "ติดต่อฝ่ายขาย","uri": "https://line.me/ti/p/~@698cynyd"},
		"style": "primary","color": "#00A1FF"
	  }
	]
  }
}
	return bubble

def flexobj(data):
	carousel = {"type": "carousel","contents": []}
	for row in data:
		bubbleset = bubble(str(row["name"]),str(row["image"]),str(row["address"]),str(row["neighborhood"]),str(row["price"]),str(row["url"]),str(row["distance"]))
		carousel["contents"].append(bubbleset)
	return carousel
