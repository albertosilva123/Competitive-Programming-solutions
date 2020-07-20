#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

/*
This solution is a bit less naive than Jeroen's (I think)
We do all the preprocessing: determine which groups of frogs matter
and compute the size of the biggest tower.
Then we "simulate" the jumping for the remaining frogs, multiple jumps at a time.
This runs quite fast!
*/

using namespace std;

using ll = long long unsigned int;

// NAIVE, should do a CRT here
pair<ll, ll> merge(pair<ll, ll> lhs, pair<ll, ll> rhs) {
    if (lhs.second == rhs.second) {
        return {lhs.first * rhs.first, lhs.second};
    }
    
    if (lhs.second > rhs.second) {
        return merge(lhs, {rhs.first, rhs.second + rhs.first});
    } else {
        return merge({lhs.first, lhs.second + lhs.first}, rhs);
    }
}

int main () {
    ios::sync_with_stdio(false); cin.tie(0);
    ll n;
    cin >> n;

    // for each jump distance, gather all frogs
    unordered_map<ll, vector<ll>> classes;
    for (int i = 0; i < n; ++i) {
        ll x, d;
        cin >> x >> d;

        classes[d].push_back(x);
    }

    // for each jump distance we have a starting position
    vector<pair<ll, vector<ll>>> dists_locs;
    ll size_of_tower = 0;
    for (const auto p : classes) {
        const auto d = p.first;

        // for each starting position, gather the number of frogs and biggest location
        // vector does not work, d is too big
        unordered_map<ll, pair<ll, ll>> mod_classes;

        ll biggest_cls = 0;

        for (const auto x : p.second) {
            const auto clas = x % d;
            auto & p = mod_classes[clas];
            p.first++;
            p.second = max(p.second, x);

            if (p.first > biggest_cls) {
                biggest_cls = p.first;
            }
        }

        vector<ll> biggest_idx;
        for (const auto p : mod_classes) {
            if (p.second.first == biggest_cls) {
                biggest_idx.push_back(p.second.second);
            }
        }

        assert(!biggest_idx.empty());
        size_of_tower += biggest_cls;
        dists_locs.emplace_back(d, biggest_idx);
    }

    vector<pair<ll, ll>> chain;
    chain.reserve(dists_locs.size());

    function<ll(int)> recurse = [&](int i) {
        if (i < dists_locs.size()) {
            ll mini = ll(-1); // unsigned
            for (const auto & p : dists_locs[i].second) {
                chain.emplace_back(dists_locs[i].first, p);
                mini = min(mini, recurse(i+1));
                assert(mini != ll(-1));
                chain.pop_back();
            }
            return mini;
        } else {
            pair<ll, ll> acc = chain[0];
            for (int j = 1; j < chain.size(); ++j) {
                acc = merge(acc, chain[j]);
            }
            return acc.second;
        }
    };

    const auto ans = recurse(0);
    assert(ans != ll(-1));

    cout << ans << ' ' << size_of_tower << endl;
}