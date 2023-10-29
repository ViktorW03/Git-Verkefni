import string
def read_docs(filename):
    try:
        with open(filename, 'r') as file:
            content = file.readlines()
        return content
    except FileNotFoundError:
        print("File not found.")
        return None

def open_doc(content):
    doc_dict = {}
    doc = []
    doc_num = 1  
    for line in content:
        if line.strip() == "<END OF DOCUMENT>":
            doc_key = f"Document_{doc_num}"
            doc_dict[doc_key] = "\n".join(doc)
            doc = []
            doc_num += 1
        else:
            doc.append(line.strip())
    return doc_dict

import string

def find_doc(doc_dict, lines):
    matching_docs = []

    lines_lower = [''.join(ch for ch in line.lower() if ch not in string.punctuation) for line in lines]

    for key, doc_content in doc_dict.items():

        words_in_doc = set(''.join(ch for ch in word if ch not in string.punctuation) for word in doc_content.lower().split())
        
        if set(lines_lower).issubset(words_in_doc):
            matching_docs.append(key)

    return matching_docs




def display_doc(doc_dict, doc_key):
    if doc_key in doc_dict:
        doc_number = doc_key.split('_')[1]
        print(f"Document #{doc_number}:")
        print(doc_dict[doc_key])
    else:
        print("No match")


def main():
    filename = input().strip()  
    content = read_docs(filename)
    
    if content:
        doc_dict = open_doc(content)

    if not doc_dict:
        return

    while True:
        action = input().strip()  

        if action == "search":
            terms = input().split() 
            matching_docs = find_doc(doc_dict, terms)  
            
            if matching_docs:
                
                matching_numbers = " ".join([doc.split('_')[1] for doc in matching_docs])
                print("Documents matching search:", matching_numbers)
            else:
                print("No match")

        elif action == "print":
            doc_num = input().strip()
            if doc_num.isdigit():
                doc_key = f"Document_{doc_num}"
                display_doc(doc_dict, doc_key)
            else:
                print("Invalid document number.")

        elif action == "quit":
            break

if __name__ == "__main__":
    main()
