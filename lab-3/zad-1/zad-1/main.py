from subject import Subject
from observer import ProgressBarObserver


def main():
    progr_bar_val = 100
    sub = Subject(progr_bar_val)
    obs = ProgressBarObserver(progr_bar_val)
    sub.add_observer(obs)
    sub.perform()


if __name__ == '__main__':
    main()
