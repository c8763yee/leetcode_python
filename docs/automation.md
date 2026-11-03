# 每日自動同步

[Sync LeetCode](../.github/workflows/sync-leetcode.yml) 每天以 `0 8 * * *`、`Asia/Taipei`（UTC+8）排程，擷取 `c8763yee` 每題各語言最新的 Accepted，更新解答、README 與提交索引後推送至預設分支。也可在 GitHub 的 Actions → Sync LeetCode → Run workflow 手動執行。

GitHub 排程可能延遲，不保證準時 08:00；workflow 必須位於預設分支。公開 repository 若 60 天無活動，GitHub 可能停用排程。

## 設定 Secrets

在 repository 的 **Settings → Secrets and variables → Actions → New repository secret** 建立：

| 名稱 | 內容 |
|---|---|
| `LEETCODE_SESSION` | 登入 c8763yee 後的完整 `LEETCODE_SESSION` Cookie 值 |
| `LEETCODE_CSRF_TOKEN` | 同一個登入工作階段的 `csrftoken` Cookie 值 |
| `DISCORD_WEBHOOK_URL` | Discord 頻道 → 編輯頻道 → 整合 → Webhooks → 複製 Webhook URL |

本機 `.env.leetcode` 不會自動上傳成 Secrets。Cookie 過期時，請更新這兩個 LeetCode Secrets。Workflow 使用環境變數讀取 Cookie，不會將登入資訊寫入 repository 或快取。Secrets 環境變數優先於本機登入檔案。

Workflow 已宣告 `contents: write`，不需額外的 PAT。若組織政策或預設分支保護規則禁止 GitHub Actions 直接推送，推送仍會失敗，需調整該 repository 的規則以允許預期的自動更新。

## 快取與失敗通知

每次執行重新讀取完整提交清單，只用 cache 避免重複下載既有提交的詳細資料；不使用 `--resume` 的舊歷史快照。沒有新內容時不建立 commit。同步失敗時不會執行 commit/push。

失敗通知為獨立 job，透過 `needs.sync.result == 'failure'` 篩選，涵蓋同步 job 的下載、驗證、commit/push 失敗，以及執行逾時。成功或手動取消不發通知。Discord 訊息包含 repository 名稱與該次執行連結；沒有設定 Webhook Secret 或 Discord 無法連線時，通知 job 也會顯示失敗。

若 GitHub 本身尚未排入工作、Actions 服務中斷或 workflow YAML 無效，工作無法啟動，就無法靠此 workflow 自行通知。

## GitHub 原生 webhook 能否只送失敗？

Repository webhook 可以選擇 `workflow_run` 事件，但無法在 webhook 設定中只篩選失敗。接收端需要檢查 `action == "completed"` 及 `workflow_run.conclusion == "failure"`。另一種方式是使用 `workflow_run` 觸發通知 workflow，再用相同條件篩選。

本專案使用同步 workflow 內的條件式通知 job，直接發送 Discord 格式的訊息，不需額外的 webhook 接收服務。

參考：[GitHub 排程與時區](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)、[workflow_run webhook](https://docs.github.com/en/webhooks/webhook-events-and-payloads#workflow_run)、[Discord Webhook](https://docs.discord.com/developers/resources/webhook)。
