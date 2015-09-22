Title: Archiving Banking Transactions
Status: draft
Tags: Process

don't trust banks to always provide transaction history forever
yearly CSVs separated by account
all banks I use so far provide CSV downloads (HSBC only seem to provide PDFs for legacy (3months or older) transactions) but usually this is for a period of time and I wanted to separate them

started with natwest as main bank, turns out they spoil me - one download of all accounts in one csv - awk is *great* at dealing with this

scripts are predominantly data redirection around a central awk command as a rough rule of thumb
