

typedef struct {
    long long* balance;
    int account;
} Bank;

Bank* bankCreate(long long* balance, int balanceSize) {
    Bank* newBank = malloc(sizeof(Bank));
    newBank->balance = balance;
    newBank->account = balanceSize;
    return newBank;
}

bool bankTransfer(Bank* obj, int account1, int account2, long long money) {
    if (account1 > obj->account ||
            account2 > obj->account ||
            obj->balance[account1-1] < money)
        return false;
    obj->balance[account2-1] += money;
    obj->balance[account1-1] -= money;
    return true;
}

bool bankDeposit(Bank* obj, int account, long long money) {
    if (account > obj->account)
        return false;
    obj->balance[account-1] += money;
    return true;
}

bool bankWithdraw(Bank* obj, int account, long long money) {
    if (account > obj->account||obj->balance[account-1] < money)
        return false;
    obj->balance[account-1] -= money;
    return true;
}

void bankFree(Bank* obj) {
    free(obj->balance);
    free(obj);
}

/**
 * Your Bank struct will be instantiated and called as such:
 * Bank* obj = bankCreate(balance, balanceSize);
 * bool param_1 = bankTransfer(obj, account1, account2, money);

 * bool param_2 = bankDeposit(obj, account, money);

 * bool param_3 = bankWithdraw(obj, account, money);

 * bankFree(obj);
*/