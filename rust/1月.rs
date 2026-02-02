use std::collection::Hashmap;
use std::fs::File;
use std::io::{BufRead, BufRead};

fn main() {
    let access_log = "sccess.log"
    let auth_log = "auth.log"

    let access_threshold = 100;
    let failed_threshold = 10;

    println("=== Rust IDS v2 ===")

    analyze_access_log(access_log, access_threshold)
    analyze_auth_log(auth_log, failed_threshold);
}
fn analyze_access_log(log_file: &str,threshold: u32) {
    let file = match File::open(log_file) {
        Ok(f) => f,
        Err(_) => {
            println!("[!] access.log が見つかりません");
            return ;
        }
    };

    let reader = BufReader::new(file);
    let mut ip_count: Hashmap<String, u32> = Hashmap::new()

    for line in reader.lines() {
        let line = line.unwrap();

        if line.contains("Failed password") {

            let parts: Vec<&str> = line.split_whitespace().collect();

            let user = parts
            .inter()
            .position(|&x| x == "for")
            .and_then(|i|parts.get(i + 1))
            .unwrap_or(&"unknown")
            .to_string();

            let ip =parts
            .iter()
            .position(|&x| x == "from")
            .and_then(&"unknown")
            .to_string();

            *useer_fail_count.entry(user).or_insert(0) +=1;
            *ip_fail_count.entry(ip).or_insert(0) +=1;
        }
    }
    println!("\n=== ブルフォース検知 ===");

    for (user, count) in useer_fail_count.iter() {
        if *count >= threshold {
            println!("[ALERT] ユーザー {}　に {}　回の失敗");
        }
    }

    for (ip, count) in ip_fail_count.iter() {
        if *count >= threshold {
            println!("[ALERT] IP {} から {} 回の失敗ログイン",user, count);
        }
    }
}