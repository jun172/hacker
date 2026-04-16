import random
from quesrions import questions
from utils import check_answer, save_score

def play_game():
    print("🎮 Linux 基礎100問ゲームスタート! 🎮")
    score = 0
    random.shuffle(questions)
    for i, q in enumerate(questions,1):
        print(f"\n問題 {i}: {q['question']}")
        
        # 選択肢をシャッフルして番号を変える
        opts = q['options'].copy()
        random.shuffle(opts)
        
        for idx, opt in enumerate(opts,1):
            print(f"{idx}.{opt}")
        answer = input("答えの番号を入力してください: ")
        
        if opts[int(answer)-1] == q['answer']:
            print("✅ 正解！")
            score += 1
        else:
            print(f"❌ 不正解！正解は {q['answer']} です。")
    
    username = input("\nユーザー名を入力してください: ")
    save_score(username,score)
    print(f"\n{username}さんのスコア: {score}/{len(questions)}")
    
if __name__ == "__main__":
    play_game()