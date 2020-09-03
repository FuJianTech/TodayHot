


class Machine(object):

    def __init__(self, name, position, date):
        self.name = name
        self.position = position
        self.date = date

    def getinfo(self):
        return self.name, self.position

    def getdate(self):
        return self.date


class Server(Machine):

    def __init__(self, name, position, date, ipaddr):
        self.ipaddr = ipaddr
        super(Server, self).__init__(name, position, date)

    def getaddr(self):
        return self.ipaddr
if __name__ == '__main__':

    s = Server('cnsz003621', 'position1', '2017/02/23', '10.10.2.77')
    r = s.getinfo()
r2 = s.getaddr()
print(r, r2)



data_dict ={
"layer_res_id": "Library://建筑/图层/JT.LayerDefinition",
"info_list":"POLYGON((-2008392.1372189675 4851482.090147233, -2008408.5816488934 4851511.56189861, -2008464.2117236583 4851475.5584699195, -2008458.6851865863 4851464.488297083))   "
}


