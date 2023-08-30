from abc import ABC, abstractmethod

class IAnimal:
    
    @abstractmethod
    def falar(self):
        """defina na classe da filha"""
        
    @abstractmethod
    def andar(self):
        """difina na classe da filha"""
        
class Cachorro(IAnimal):
    def falar(self):
        print("au")
        
    def andar(self):
        print("andar")