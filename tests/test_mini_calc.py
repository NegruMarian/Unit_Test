from app.mini_calc import MiniCalc
class TestMiniCalc:

    def setup_method(self):
        self.calc = MiniCalc(5,5)

    def teardown_method(self):
        print('Testul a fost finalizat!')

    def test_init(self):
        assert self.calc.a==5,"a nu are valoarea corecta"
        assert self.calc.b==5,'b nu are valoarea corecta'


    def test_adunare(self):
        assert self.calc.adunare()==10,"adunarea nu se face corect"

    def test_scadere(self):
        assert self.calc.scadere()==0,'Scaderea nu se face corect'

    def test_inmultire(self):
        assert self.calc.inmultire()==25,'Inmulirea nu se face corect'

    def test_impartire(self):
        assert  self.calc.impartire()==1,'Impartirea nu se face corect'




