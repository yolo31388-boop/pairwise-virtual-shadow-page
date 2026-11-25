# pairwise-virtual-shadow-page

## 领域

游戏、图形与多媒体

## 主题

虚拟阴影贴图页缓存

## 说明

页独占、回读置有效与重分配清历史。

初始状态下 `graphics/vsm_page.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
