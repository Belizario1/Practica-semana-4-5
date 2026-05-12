#include <iostream>
using namespace std;

class Config {
private:
    static Config* instance;
    Config() {} // Constructor privado
public:
    static Config* getInstance() {
        if (!instance) instance = new Config();
        return instance;
    }
    void showMessage() { cout << "Configuracion global cargada.\n"; }
};
Config* Config::instance = nullptr;

int main() {
    Config* obj1 = Config::getInstance();
    Config* obj2 = Config::getInstance();
    obj1->showMessage();
    cout << "Son iguales? " << (obj1 == obj2) << endl;
    return 0;
}