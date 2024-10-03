[ Fri Sep 20 18:44:00 2024 ] Eval epoch: 10
/data/hranjb/ST-TR/code/main.py:785: UserWarning: volatile was removed and now has no effect. Use `with torch.no_grad():` instead.
  data = Variable(
/data/hranjb/ST-TR/code/main.py:789: UserWarning: volatile was removed and now has no effect. Use `with torch.no_grad():` instead.
  label = Variable(
[ Fri Sep 20 18:44:04 2024 ]    Mean val loss of 113 batches: 648729801691.7522.
Here are the just predicted labels:  tensor([98, 98, 98, 98, 98, 98, 98], device='cuda:0')
Here are the correct labels:  tensor([59, 62, 65,  9, 44, 82, 29], device='cuda:0')
Total samples seen so far:  903

Validation: Epoch [9/120], Samples [4.0/903], Loss: 46701580288.0, Validation Accuracy: 0.4429678848283499