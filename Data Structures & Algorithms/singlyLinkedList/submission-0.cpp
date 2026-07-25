class LinkedList {
struct Node{
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};
private:
    Node* head;
    Node* tail;
public:
    LinkedList() {
        head = tail = nullptr;
    }

    int get(int index) {
        Node* curr = head;
        int count =0;
        while(curr){
            if(count == index){
                return curr->data;
            }
            count++;
            curr = curr->next;
        }
        return -1;
    }

    void insertHead(int val) {
        Node* newNode = new Node(val);
        if(head == nullptr){
            head = tail = newNode;
        }else{
            newNode->next = head;
            head = newNode;
        }
    }
    
    void insertTail(int val) {
        Node* newNode = new Node(val);
        if(tail == nullptr){
            head = tail = newNode;
        }
        else{
            tail->next = newNode;
            tail = newNode;
        }
    }

    bool remove(int index) {
        if(!head) return false;
        // case 1 : index == 0;
        if(index == 0){
            Node* temp = head;
            head = head->next;
            if(!head){
                tail = nullptr;
            }
            delete temp;
            return true;
        }
        // case 2 : 
        Node* curr = head;
        int cnt = 0;
        while(curr && curr->next && cnt < index-1){
            curr = curr->next;
            cnt++;
        }
        if(!curr || !curr->next){
            return false;
        }   
        Node* NodeToDelete = curr->next;
        curr->next = curr->next->next;
        // case 3 : if happens to be the tail
        if(NodeToDelete == tail){
            tail = curr;
        }
        delete NodeToDelete;
        return true;
    }

    vector<int> getValues() {
        vector<int> res;
        Node* curr = head;
        while(curr){
            res.push_back(curr->data);
            curr = curr->next;
        }
        return res;
    }
};
