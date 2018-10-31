from datetime import date, datetime, timedelta
from operator import add
from dateutil.relativedelta import relativedelta
from rest_framework.views import APIView
from rest_framework.response import Response

from . import data as d


class DailyTotalsForPeriod(APIView):
    # TODO +role permission (CFO)
    permission_classes = ()

    def get(self, request, y_0, m_0, d_0, y_1, m_1, d_1):
        n_ = datetime.now()

        date_1_ = datetime(int(y_1 or n_.year), int(m_1 or n_.month), int(d_1 or n_.day), 23, 59, 59)

        if not (y_0 or m_0 or d_0):
            date_0_ = date_1_ + relativedelta(months=-1)
            date_0_ = datetime(date_0_.year, date_0_.month, 1)
        else:
            date_0_ = datetime(int(y_0 or n_.year), int(m_0 or n_.month), int(d_0 or n_.day))

        return Response({
            "date_0": date_0_,
            "date_1": date_1_,
            # "headings": ["Date", "Act.S.V.", "Exp.S.V.", "Dis.S.V."],
            "daily_totals": d.daily_totals_for_period(date_0_, date_1_),
        })


        # t_ = datetime.now()

        # raw_ = d.daily_totals_for_period(date_0_, date_1_)

        # ft_ = datetime.now() - t_
        # t_ = datetime.now()

        # sd_ = {"id": None, "tots": [0, 0, 0], "rows": []}
        # cr_ = {"id": None, "tots": [0, 0, 0], "rows": []}
        # pm_ = {"id": None, "tots": [0, 0, 0], "rows": []}

        # for r_ in raw_:

        #     if sd_["id"] != r_["sdate"] or cr_["id"] != r_["cr_ident"] or pm_["id"] != r_["pm"]:
        #         # payment
        #         if pm_["id"]:
        #             pm_["rows"].append({
        #                 "sdate": sd_["id"],
        #                 "cashreg": cr_["id"],
        #                 "payment": pm_["id"],
        #                 "act_sv": pm_["tots"][0],
        #                 "exp_sv": pm_["tots"][1],
        #                 "dis_sv": pm_["tots"][2]
        #             })
        #         pm_["id"] = r_["pm"]
        #         pm_["tots"] = [0, 0, 0]

        #     if sd_["id"] != r_["sdate"] or cr_["id"] != r_["cr_ident"]:
        #         # cashreg
        #         if cr_["id"]:
        #             cr_["rows"].append({
        #                 "sdate": sd_["id"],
        #                 "cashreg": cr_["id"],
        #                 "act_sv": cr_["tots"][0],
        #                 "exp_sv": cr_["tots"][1],
        #                 "dis_sv": cr_["tots"][2]
        #             })
        #             cr_["rows"].append({"group": pm_["rows"]})
        #             pm_["rows"] = []
        #         cr_["id"] = r_["cr_ident"]
        #         cr_["tots"] = [0, 0, 0]

        #     if sd_["id"] != r_["sdate"]:
        #         # sdate
        #         if sd_["id"]:
        #             sd_["rows"].append({
        #                 "sdate": sd_["id"],
        #                 "act_sv": sd_["tots"][0],
        #                 "exp_sv": sd_["tots"][1],
        #                 "dis_sv": sd_["tots"][2]
        #             })
        #             sd_["rows"].append({"group": cr_["rows"]})
        #             cr_["rows"] = []
        #         sd_["id"] = r_["sdate"]
        #         sd_["tots"] = [0, 0, 0]

        #     sd_["tots"] = list(map(add, sd_["tots"], [r_["act_sv"], r_["exp_sv"], r_["dis_sv"]]))
        #     cr_["tots"] = list(map(add, cr_["tots"], [r_["act_sv"], r_["exp_sv"], r_["dis_sv"]]))
        #     pm_["tots"] = list(map(add, pm_["tots"], [r_["act_sv"], r_["exp_sv"], r_["dis_sv"]]))

        # # payment
        # if pm_["id"]:
        #     pm_["rows"].append({
        #         "sdate": sd_["id"],
        #         "cashreg": cr_["id"],
        #         "payment": pm_["id"],
        #         "act_sv": pm_["tots"][0],
        #         "exp_sv": pm_["tots"][1],
        #         "dis_sv": pm_["tots"][2]
        #     })
        # # cashreg
        # if cr_["id"]:
        #     cr_["rows"].append({
        #         "sdate": sd_["id"],
        #         "cashreg": cr_["id"],
        #         "act_sv": cr_["tots"][0],
        #         "exp_sv": cr_["tots"][1],
        #         "dis_sv": cr_["tots"][2]
        #     })
        #     cr_["rows"].append({"group": pm_["rows"]})
        #     pm_["rows"] = []
        # # sdate
        # if sd_["id"]:
        #     sd_["rows"].append({
        #         "sdate": sd_["id"],
        #         "act_sv": sd_["tots"][0],
        #         "exp_sv": sd_["tots"][1],
        #         "dis_sv": sd_["tots"][2]
        #     })
        #     sd_["rows"].append({"group": cr_["rows"]})
        #     cr_["rows"] = []

        # pt_ = datetime.now() - t_

        # return Response({
        #     "date_0": date_0_,
        #     "date_1": date_1_,
        #     "headings": ["Date", "Act.S.V.", "Exp.S.V.", "Dis.S.V."],
        #     "rows": sd_["rows"],
        # })
