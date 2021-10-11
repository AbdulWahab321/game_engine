import pygame
from time import sleep
class Game:
    def __init__(self):
        pygame.init()
        self.do = []
        self.isRunning = False
        self.bg = None
        self.onQuit = pygame.quit
        self.resolution = None
    def create_screen(self,resolution=(800,600)):
        self.resolution = resolution
        self.screen = pygame.display.set_mode(resolution)
    def set_caption(self,title,iconTitle=None):
        self.get_display().set_caption(title,icontitle=iconTitle)
    def set_bgcolor(self,rgb=(0,0,0)):
        self.screen.fill(rgb)   
    def set_icon(self,path):
        path = pygame.image.load(path)
        self.get_display().set_icon(path)
    def get_size(self):
        return self.screen.get_size()    
    def get_width(self):
        size = self.get_size()
        return size[0]  
    def get_height(self):
        size = self.get_size()
        return size[1]
    def background_image(self,image_path):
        mslf = self
        class Background:
            def __init__(self):
                self.image = pygame.image.load(image_path)
            def draw(self):    
                image = pygame.transform.scale(self.image,mslf.get_size())
                mslf.screen.blit(image,(0,0))
        return Background()   
    def sprite(self,color=(0,155,120),position=(0,0),size=(100,100)):
        mslf = self
        class Sprite:
            def __init__(self,color,position,size):
                x, y = position
                width, height = size
                self.x = x
                self.color = color
                self.y = y
                self.width = width
                self.height = height
                self.movementDisabled = False
            def draw(self):
                rect = pygame.draw.rect(mslf.screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
                return rect    
            def setX(self,xpos):
                self.x = xpos
            def setY(self,ypos):
                self.y = ypos
            def setPosition(self,position=()):
                x,y = position
                self.x = x
                self.y = y 
            def get_position(self):
                return (self.x,self.y)
            def get_XPosition(self):
                return self.x
            def get_YPosition(self):
                return self.y                
            def setSize(self,size):    
                self.size = size  
                self.image = pygame.transform.scale(self.image,size)
            def diableMovement(self):
                self.movementDisabled = True
            def enableMovement(self):
                self.movementDisabled = False        
            def moveUp(self,velocity):
                if not self.movementDisabled:self.y-=velocity
            def moveDown(self,velocity):
                if not self.movementDisabled:self.y+=velocity
            def moveRight(self,velocity):
                if not self.movementDisabled:self.x-=velocity
            def moveLeft(self,velocity):
                if not self.movementDisabled:self.x-=velocity       
            def get_size(self):
                return (self.image.get_width(),self.image.get_height())
            def get_width(self):
                return self.image.get_width()
            def shrink(self,by:int):
                self.setSize((self.get_width()//by,self.get_height()//by))    
            def get_height(self):
                return self.image.get_height()                 
            def setPosToCursorPos(self,x=True, y=True, center=False):
                if not self.cursor_pos_disabled:
                    mx,my = pygame.mouse.get_pos()
                    if size:
                        width, height = self.size
                    else:
                        width, height = self.image.get_width(), self.image.get_height()    
                    if center:
                        if x==True:
                            self.setX(mx-width/2)
                        else:
                            _string = str(x)
                            if _string.isnumeric():self.setX(x)    
                        if y==True:
                            self.setY(my-height/2)   
                        else:
                            _string = str(y)
                            self.setY(y)     
                    else:
                        if x==True:
                            self.setX(mx)
                        else:
                            _string = str(x)
                            if _string.isnumeric():self.setX(x)    
                        if y==True:
                            self.setY(my)
                        else:
                            _string = str(y)
                            self.setY(y)                              
            def disableSetPosToCursorPos(self):
                self.cursor_pos_disabled = True  
        return Sprite(color,position,size)                     
    def image_sprite(self,image_path,x,y,size=None):
        mslf = self
        class Sprite:
            def __init__(self,size):
                self.image = pygame.image.load(image_path)
                self.size = size
                self.x = x
                self.y = y
                self.collideEdges = False
                self.cursor_pos_disabled = False
                self.movementDisabled = False
            def set_collideEdges(self,collideEdges=False,x=True,y=True):
                if collideEdges:
                    self.collideEdges= {"x":x,"y":y}    
            def draw(self):
                image = self.image
                if size:
                    self.image = pygame.transform.scale(image,self.size)
                mslf.screen.blit(self.image,(self.x, self.y))
                if self.collideEdges:
                    if self.collideEdges.get("x") == True:
                        if self.x >= mslf.resolution[0]-self.get_width():
                            self.setX(mslf.resolution[0]-self.get_width())
                    if self.collideEdges.get("y") == True:
                        if self.y >= mslf.resolution[1]-self.get_height():
                            self.setX(mslf.resolution[1]-self.get_height())                                
            def setX(self,xpos):
                self.x = xpos
            def setY(self,ypos):
                self.y = ypos
            def setPosition(self,position=()):
                x,y = position
                self.x = x
                self.y = y 
            def get_position(self):
                return (self.x,self.y)
            def get_XPosition(self):
                return self.x
            def get_YPosition(self):
                return self.y                
            def setSize(self,size):    
                self.size = size  
                self.image = pygame.transform.scale(self.image,size)
            def disableMovement(self):
                self.movementDisabled = True
            def enableMovement(self):
                self.movementDisabled = False        
            def moveUp(self,velocity):
                if not self.movementDisabled:self.y-=velocity
            def moveDown(self,velocity):
                if not self.movementDisabled:self.y+=velocity
            def moveRight(self,velocity):
                if not self.movementDisabled:self.x-=velocity
            def moveLeft(self,velocity):
                if not self.movementDisabled:self.x-=velocity       
            def get_size(self):
                return (self.image.get_width(),self.image.get_height())
            def get_width(self):
                return self.image.get_width()
            def shrink(self,by:int):
                self.setSize((self.get_width()//by,self.get_height()//by))    
            def get_height(self):
                return self.image.get_height()                 
            def setPosToCursorPos(self,x=True, y=True, center=False):
                if not self.cursor_pos_disabled:
                    mx,my = pygame.mouse.get_pos()
                    if size:
                        width, height = self.size
                    else:
                        width, height = self.image.get_width(), self.image.get_height()    
                    if center:
                        if x==True:
                            self.setX(mx-width/2)
                        else:
                            _string = str(x)
                            if _string.isnumeric():self.setX(x)    
                        if y==True:
                            self.setY(my-height/2)   
                        else:
                            _string = str(y)
                            self.setY(y)     
                    else:
                        if x==True:
                            self.setX(mx)
                        else:
                            _string = str(x)
                            if _string.isnumeric():self.setX(x)    
                        if y==True:
                            self.setY(my)
                        else:
                            _string = str(y)
                            self.setY(y)                              
            def disableSetPosToCursorPos(self):
                self.cursor_pos_disabled = True        
        sprite = Sprite(size)        
        return sprite       
    def key_pressed(self, key):
        self.isRunning = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.onQuit:return self.onQuit() 
            if event.type == pygame.KEYDOWN:
                if event.key == key:return True
            elif event.type == pygame.KEYUP:
                if event.key == key:return False         
        return self.get_display().update()                    
    def get_display(self):
        return pygame.display    
    def create_image(self,path):
        self.screen.blit()    
    def get_events():
        return pygame.event.get()      
    def run(self):
        if not self.isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if self.onQuit:return self.onQuit()    
            return self.get_display().update()         